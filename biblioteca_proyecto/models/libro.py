from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class BibliotecaLibro(models.Model):
    _name = 'biblioteca_proyecto.libro'
    _description = 'Libro de la Biblioteca'
    
    # Campo obligatorio (el nombre del registro)
    name = fields.Char(string='Título', required=True)
    
    # Campos de información básica
    autor = fields.Char(string='Autor', help="Nombre completo del autor")
    isbn = fields.Char(string='ISBN', copy=False)
    fecha_publicacion = fields.Date(string='Fecha de Publicación')
    
    # Campo numérico
    paginas = fields.Integer(string='Número de Páginas')
    
    # Campo de selección (Estado del libro)
    state = fields.Selection([
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
        ('dañado', 'En Reparación'),
        ('perdido', 'Perdido')
    ], string='Estado', default='disponible', tracking=True)
    
    # Campo booleano
    es_digital = fields.Boolean(string='¿Es formato digital?', default=False)
    
    # Campo de texto largo
    descripcion = fields.Html(string='Sinopsis')

    # Ejemplo de una restricción (Python Constraint)
    @api.constrains('paginas')
    def _check_paginas_positivas(self):
        for record in self:
            if record.paginas <= 0:
                raise ValidationError("El libro debe tener un número positivo de páginas.")
            
    # Método para cambiar el estado del libro a 'prestado'
    def action_prestar(self):
        for record in self:
            if record.state == 'disponible':
                record.state = 'prestado'
            else:
                raise UserError(("El libro '%s' no se encuentra disponible actualmente.") % record.name)
                continue