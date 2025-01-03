# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SoporteTecnico(models.Model):
    _name = 'soporte.tecnico'
    _inherit = ['soporte.tecnico', 'mail.thread', 'mail.activity.mixin']
    _description = 'Modelo para almacenar las personas que trabajan en las incidencias.'

    tipo = fields.Selection(
        string='Tipo',
        selection=[
            ('0', 'Técnico General'),
            ('1', 'Técnico Hardware'),
            ('2', 'Técnico Software'),
            ('3', 'Técnico Redes'),
            ],
        default='0',
        )
    
    