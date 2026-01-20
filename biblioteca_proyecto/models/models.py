# from odoo import models, fields, api


# class biblioteca_proyecto(models.Model):
#     _name = 'biblioteca_proyecto.biblioteca_proyecto'
#     _description = 'biblioteca_proyecto.biblioteca_proyecto'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

