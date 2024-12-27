# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SoporteTecnico(models.Model):
    _name = 'soporte.tecnico'
    _description = 'Modelo para almacenar las personas que trabajan en las incidencias'

    name = fields.Char(string='Nombre', required=True)
    