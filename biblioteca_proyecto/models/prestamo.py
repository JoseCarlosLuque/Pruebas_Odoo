from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date
import logging

class BibliotecaPrestamo(models.Model):
    _name = 'biblioteca_proyecto.prestamo'
    _description = 'Registro de Préstamo'

    usuario_id = fields.Many2one('biblioteca_proyecto.usuario', string='Usuario', required=True)
    libro_id = fields.Many2one('biblioteca_proyecto.libro', string='Libro', required=True)
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('proceso', 'En curso'),
        ('devuelto', 'Devuelto')
    ], default='borrador')
    
    fecha_prestamo = fields.Date(string='Fecha de Préstamo', default=fields.Date.context_today, required=True)

    fecha_devolucion_prevista = fields.Date(
        string='Fecha Prevista de Devolución', 
        required=True,
        default=lambda self: fields.Date.add(fields.Date.today(), days=14) # Por defecto 2 semanas
    )
    
    fecha_devolucion_real = fields.Date(string='Fecha Real de Devolución')
    
    fuera_de_plazo = fields.Boolean(
        string='Fuera de Plazo', 
        compute='_compute_es_tarde', 
        store=True # Para almacenar el valor en la base de datos y no tener que calcularlo cada vez.
    )

    @api.depends('fecha_devolucion_prevista', 'state')
    def _compute_es_tarde(self):
        hoy = date.today()
        for record in self:
            if record.state == 'proceso' and record.fecha_devolucion_prevista < hoy:
                record.fuera_de_plazo = True
            else:
                record.fuera_de_plazo = False

    def run_check_retrasos_cron(self):
        """Método que llamará el Cron Job"""
        hoy = fields.Date.today()
        # Buscamos préstamos en proceso que han vencido y no están marcados como retrasados
        prestamos_vencidos = self.search([
            ('state', '=', 'proceso'),
            ('fecha_devolucion_prevista', '<', hoy),
            ('fuera_de_plazo', '=', False)
        ])
        
        for prestamo in prestamos_vencidos:
            # Al actualizar esto, el store=True se guardará en la DB
            prestamo.fuera_de_plazo = True
            
            # 1. Registro en el log (para que veas que funciona)
            _logger.info(f"Cron: Préstamo {prestamo.id} del usuario {prestamo.usuario_id.name} marcado como retrasado.")
            
            # 2. Envío de notificación (Chatter)
            # Esto enviará un correo si el usuario es seguidor o tiene email configurado
            prestamo.message_post(
                body=f"⚠️ **Notificación Automática**: El plazo para devolver el libro '{prestamo.libro_id.name}' venció el {prestamo.fecha_devolucion_prevista}. Por favor, proceda a su devolución.",
                subtype_xmlid="mail.mt_comment"
            )

    def action_confirmar_prestamo(self):
        for record in self:
            if record.libro_id.state != 'disponible':
                raise ValidationError(_("El libro %s no está disponible para préstamo.") % record.libro_id.name)
            
            # Cambiamos el estado de ambos modelos
            record.libro_id.state = 'prestado'
            record.state = 'proceso'

    def action_devolucion(self):
        for record in self:
            # 1. Cambiamos el estado del registro de préstamo
            record.state = 'devuelto'
            record.fecha_devolucion_real = fields.Date.today()

            # 2. Cambiamos el estado del libro vinculado
            # Usamos la referencia socio_id.libro_id (tu Foreign Key)
            record.libro_id.state = 'disponible'
    
    # Método dummy para evitar errores en vistas
    def action_dummy(self):
        return True