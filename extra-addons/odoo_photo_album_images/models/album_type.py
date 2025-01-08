# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AlbumType(models.Model):
    _name = 'album.type'
    _description = 'Album Type'
    
    name = fields.Char(
        string='Name',
        required=True
    )
    