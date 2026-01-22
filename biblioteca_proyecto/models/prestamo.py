from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date

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
    