# -*- coding: utf-8 -*-
# from odoo import http


# class LgpmMaintenance(http.Controller):
#     @http.route('/lgpm_maintenance/lgpm_maintenance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lgpm_maintenance/lgpm_maintenance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lgpm_maintenance.listing', {
#             'root': '/lgpm_maintenance/lgpm_maintenance',
#             'objects': http.request.env['lgpm_maintenance.lgpm_maintenance'].search([]),
#         })

#     @http.route('/lgpm_maintenance/lgpm_maintenance/objects/<model("lgpm_maintenance.lgpm_maintenance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lgpm_maintenance.object', {
#             'object': obj
#         })
