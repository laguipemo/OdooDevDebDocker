# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PhotoAlbumImageLines(models.Model):
    _name = 'photo.album.image.lines'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Photo Album Image Lines'
    _rec_name = 'description'


    custom_image = fields.Binary(
        string="Photo", 
        required=True
    )
    name = fields.Char(
        related='custom_image_id.name',
        string='Name',
    )
    custom_image_id = fields.Many2one(
        'photo.album.image',
        string="Photo Album",
        copy=False    
    )
    description = fields.Char(
        string='Photo Detail',
    )


    