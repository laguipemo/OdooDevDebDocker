# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SoporteIncidencia(models.Model):
    '''Modelo para la gestión de incidencias'''
    _name = 'soporte.incidencia'
    _description = 'Modelo para la gestión de incidencias'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Html(
        string='Description',
        help='Explicación de la incidencia ocurrida de forma breve')
    priority = fields.Integer(
        string='Prioridad',
        default=1,
        help='Prioridad de la incidencia (1-10). Valor mayor que 7 es urgente'
        )
    urgent = fields.Boolean(
        string='Urgente',
        default=False,
        help='Se considera urgente si priorida >= 7'
    )

    ubicacion = fields.Selection(
        string='Ubicacion',
        selection=[
            ('1', 'Aula 1'),
            ('2', 'Aula 2')
            ]
        )

    closed = fields.Boolean(string='Cerrada', default=False)

    archivo = fields.Binary(string='Archivo adjunto')

    foto = fields.Image(
        string='Foto',
        max_width=250,
        max_height=250
        )

    fecha_creacion = fields.Datetime(
        string='Fecha de creación',
        default=fields.Datetime.now
        )

    fecha_modificacion = fields.Date(
        string='Fecha última modificación',
        default=fields.Date.today
        )
