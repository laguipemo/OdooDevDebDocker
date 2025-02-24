# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LgpmMaintenanceSatSignatures(models.Model):
    _name = 'lgpm_maintenance.sat_signatures'
    _description = 'Sat resposabilities signatures'

    RESPONSABILITIES = [
        ('admin', 'Administración'),
        ('sat', 'Responsable SAT'),
        ('prev', 'Responsable Prevención'),
    ]

    name = fields.Char(
        string='Nombre del firmante',
        required=True,
    )
    responsability = fields.Selection(
        string='Responsabilidad',
        selection=RESPONSABILITIES,
        required=True
    )
    signature = fields.Image(
        string='Firma',
        required=True,
    )
