# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
import re


_logger = logging.getLogger(__name__)

class SoporteTecnico(models.Model):
    _name = 'soporte.tecnico'
    _inherit = ['soporte.tecnico', 'mail.thread', 'mail.activity.mixin']
    _description = 'Modelo para almacenar las personas que trabajan en las incidencias.'

    dni = fields.Char(
        string='Dni',
        size=9,
        #required=True
        )

    apellido1 = fields.Char(
        string='Primer apellido',
        required=True
        )

    apellido2 = fields.Char(
        string='Segundo apellido',
        required=True
        )

    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')

    fecha_incorporacion = fields.Date(
        string='Fecha de incorporación',
        default=lambda self: fields.Datetime.now(),
        readonly=True
        )

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

    foto = fields.Image(
        string='Foto',
        max_width=200,
        max_height=200
        )

    @api.constrains('dni')
    def _check_dni(self):
        dni_pattern = re.compile("^[0-9]{8}[A-Z]$", re.IGNORECASE)
        for tecnico in self:
            if not dni_pattern.match(tecnico.dni):
                raise ValidationError("Error. El DNI debe tener 8 dígitos y una letra.")
            else:
                _logger.info("DNI correcto.")
    
    _sql_constraints = [
        ("Dni_unico", "UNIQUE(dni)", "Error. El DNI debe ser único.")
    ]