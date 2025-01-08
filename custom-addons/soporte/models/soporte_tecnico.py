# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SoporteTecnico(models.Model):
    _name = 'soporte.tecnico'
    _description = 'Modelo para almacenar las personas que trabajan en las incidencias'

    name = fields.Char(string='Nombre', required=True)
    incidencia_ids = fields.Many2many(
        string='Incidencias',
        comodel_name='soporte.incidencia',
        relation='soporte_incidencia_tecnico_rel',
        column1='tecnico_id',
        column2='incidencia_id',
        help='Incidencias en las que trabaja el técnico'
    )
    