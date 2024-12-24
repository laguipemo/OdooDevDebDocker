# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SoporteIncidencias(models.Model):
    '''Modelo para la gestión de incidencias'''
    _name = 'soporte.incidencias'
    _description = 'Modelo para la gestión de incidencias'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Description')
    priority = fields.Integer(
        string='Prioridad',
        default=1,
        help='Prioridad de la incidencia (1-10). Valor mayor que 7 es urgente'
        )
    urgent = fields.Selection(
        string='Urgente',
        selection=[('0', 'No'), ('1', 'Si')])
    closed = fields.Boolean(string='Cerrada', default=False)



# class soporte(models.Model):
#     _name = 'soporte.soporte'
#     _description = 'soporte.soporte'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
