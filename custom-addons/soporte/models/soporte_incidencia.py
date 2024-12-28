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
        string='urgent',
        compute='_compute_urgent',
        store=True,
        help='Se considera urgente si prioridad > 7')

    @api.depends('priority')
    def _compute_urgent(self):
        for incidencia in self:
            if incidencia.priority > 7:
                incidencia.urgent = True
            else:
                incidencia.urgent = False

    """ urgent = fields.Boolean(
        string='Urgente',
        default=False,
        help='Se considera urgente si prioridad > 7'
    ) """

    """ ubicacion = fields.Selection(
        string='Ubicacion',
        selection=[
            ('1', 'Aula 1'),
            ('2', 'Aula 2')
            ]
        )
 """

    ubicacion_id = fields.Many2one(
        string='Ubicación',
        comodel_name='soporte.ubicacion',
        ondelete='cascade',
        help='Ubicación de la incidencia'
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
        # la asignación directa se ejecuta solo al instalar o actualizar el modulo
        # default=fields.Datetime.now()
        # al asignarse mediante función, se ejecuta cada vez que se crea el registro
        default= lambda self: fields.Datetime.now(),
        help='Fecha en la que se crea la incidencia'
        )

    fecha_modificacion = fields.Datetime(
        string='Fecha última modificación',
        # al asignarse mediante función, se ejecuta cada vez que se crea el registro
        default= lambda self: fields.Datetime.now(),
        help='Fecha en la que se modifica la incidencia'
        )

    @api.onchange(
        'name',
        'description',
        'priority',
        'ubicacion_id',
        'closed',
        'tecnico_ids'
        )
    def _onchange_fecha_modificacion(self):
        self.fecha_modificacion = fields.Datetime.now()

    tecnico_ids = fields.Many2many(
        string='Técnicos',
        comodel_name='soporte.tecnico',
        relation='soporte_incidencia_tecnico_rel',
        column1='incidencia_id',
        column2='tecnico_id',
        help='Técnicos asignados a la incidencia'
        )
