# -*- coding: utf-8 -*-
# from odoo import http


# class Soporte(http.Controller):
#     @http.route('/soporte/soporte', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/soporte/soporte/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('soporte.listing', {
#             'root': '/soporte/soporte',
#             'objects': http.request.env['soporte.soporte'].search([]),
#         })

#     @http.route('/soporte/soporte/objects/<model("soporte.soporte"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('soporte.object', {
#             'object': obj
#         })
