# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AlbumTags(models.Model):
    _name = 'album.tags'
    _description = 'Album Tags'
    
    name = fields.Char(
        string='Name',
        required=True
    )
    code = fields.Char(
        string="Color Code",
        required=True
    )
    color = fields.Integer(
        'Color Index',
        default=0
    )

