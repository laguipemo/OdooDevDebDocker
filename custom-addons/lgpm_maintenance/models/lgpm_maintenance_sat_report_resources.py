# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LgpmMaintenanceSatReportResources(models.Model):
    _name = 'lgpm_maintenance.sat_report_resources'
    _description = 'Recursos para el informe SAT'


    name = fields.Char(
        string='Nombre de la figura',
        help='Nombre de la figura siguiendo formato ej. "Figura 1"',
        required=True,
    )
    title = fields.Text(
        string='Titulo de la figura',
        required=True
    )
    figure = fields.Image(
        string='Figura',
        required=True,
    )
