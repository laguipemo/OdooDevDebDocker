# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SoporteUbicacion(models.Model):
    _name = 'soporte.ubicacion'
    _description = 'Modelo para almacenar las ubicaciones de las incidencias'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    pabellon = fields.Selection(
        string='Pabellón',
        selection=[
            ('1', 'Pabellón Paris'),
            ('2', 'Pabellón Roma'),
            ]
        )
    planta = fields.Selection(
        string='Planta',
        selection=[
            ('0', 'Planta baja'),
            ('1', 'Planta primera'),
            ('2', 'Planta segunda'),
            ]
        )
    insidencia_ids = fields.One2many(
        string='Incidencias',
        comodel_name='soporte.incidencia',
        inverse_name='ubicacion_id',
        help='Incidencias ocurridas en esta ubicación'
        )