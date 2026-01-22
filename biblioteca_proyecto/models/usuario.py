from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class BibliotecaUsuario(models.Model):
    _name = 'biblioteca_proyecto.usuario'
    _description = 'Usuario de la biblioteca'
    _rec_name = 'dni' # Mostrar el DNI como nombre del registro en lugar del campo 'name' 

    name = fields.Char(string='Nombre Completo', required=True)
    dni = fields.Char(string='DNI', required=True, copy=False)
    _sql_constraints = [
        ('dni_unique', 'unique(dni)', '¡El DNI ya existe para otro socio!')
    ]
    email = fields.Char(string='Correo Electrónico', required=True)
    telefono = fields.Char(string='Número de Teléfono')
    fecha_registro = fields.Date(string='Fecha de Registro', default=fields.Date.context_today)

    # Acciones del Usuario:
    def action_ver_prestamos(self):
        self.ensure_one()  # Asegurarse de que solo se está trabajando con un registro
        return {
            'name': 'Préstamos del Usuario',
            'type': 'ir.actions.act_window',
            'res_model': 'biblioteca_proyecto.prestamo',
            'view_mode': 'tree,form',
            'domain': [('usuario_id', '=', self.id)],
            'context': {'default_usuario_id': self.id},
        }


    # Comprobaciones de formato
    @api.constrains('email')
    def _check_email_format(self):
        for record in self:
            if record.email and "@" not in record.email:
                raise ValidationError("El correo electrónico '%s' no tiene un formato válido." % record.email) 
        
    @api.constrains('telefono')
    def _check_telefono_format(self):
        for record in self:
            if record.telefono and not record.telefono.isdigit():
                raise ValidationError("El número de teléfono '%s' debe contener solo dígitos." % record.telefono)   
    @api.constrains('dni')
    def _check_dni_format(self):
        for record in self:
            if record.dni and len(record.dni) != 9:
                raise ValidationError("El DNI '%s' debe tener exactamente 9 caracteres." % record.dni)  
    