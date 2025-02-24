# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LgpmMaintenanceSatSignatures(models.Model):
    _name = 'lgpm_maintenance.sat_signatures'
    _description = 'Sat resposabilities signatures'

    POSITIONS = [
        ('admin', 'Administración'),
        ('sat', 'Responsable SAT'),
        ('prev', 'Responsable Prevención'),
    ]

    name = fields.Char(
        string='Nombre del firmante',
        required=True,
    )
    position = fields.Selection(
        string='Cargo',
        selection=POSITIONS,
        required=True
    )
    signature = fields.Image(
        string='Firma',
        required=True,
    )
