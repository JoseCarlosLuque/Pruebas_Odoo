# from odoo import http


# class BibliotecaProyecto(http.Controller):
#     @http.route('/biblioteca_proyecto/biblioteca_proyecto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/biblioteca_proyecto/biblioteca_proyecto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('biblioteca_proyecto.listing', {
#             'root': '/biblioteca_proyecto/biblioteca_proyecto',
#             'objects': http.request.env['biblioteca_proyecto.biblioteca_proyecto'].search([]),
#         })

#     @http.route('/biblioteca_proyecto/biblioteca_proyecto/objects/<model("biblioteca_proyecto.biblioteca_proyecto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('biblioteca_proyecto.object', {
#             'object': obj
#         })

