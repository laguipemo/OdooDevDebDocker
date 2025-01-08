# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import datetime


class PhotoAlbumImage(models.Model):
    _name = 'photo.album.image'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Photo Album Image'
    
    name = fields.Char(
        string='Name',
        required=True,
    )
    custom_image_line_ids = fields.One2many(
        'photo.album.image.lines',
        'custom_image_id',
        string="Photo Album Image Lines", 
    )
    create_date = fields.Datetime(
        "Creation Date", 
        readonly=True, 
        copy=False,
        required=False,
    )
    description = fields.Char(
        string='Description',
        required=True,
    )
    created_by = fields.Many2one(
        'res.users',
        string='Created By',
        default=lambda self: self.env.user,
        readonly=False, 
        copy=True,
    )
    custom_location = fields.Char(
        string='Album Location',
        copy=True
    )
    custom_album_tags = fields.Many2many(
        'album.tags',
        string='Album Tags',
        copy=True
    )
    custom_album_type = fields.Many2one(
        'album.type',
        string="Album Type",
        copy=True,
        required=True, 
    )
    company_id = fields.Many2one(
        'res.company',
        string="Company",
        default=lambda self: self.env.user.company_id,
        copy=True,
        groups="base.group_multi_company"
    )
    album_method = fields.Selection(
        [('internal_company', 'Internal Company Album'),
        ('external_album', 'External Album'),
        ], 
        string="Album Method", 
        default='internal_company',
        required=True, 
    )
    partner_custom_id = fields.Many2one(
        'res.partner',
        string='Customer',
        copy=True
    )

    def view_album_photos(self):
        action = self.env.ref('odoo_photo_album_images.action_custom_album_image_lines').sudo().read()[0]
        action['domain'] = [('custom_image_id','=', self.id)]
        return action


    def action_custom_email_send(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data._xmlid_lookup('odoo_photo_album_images.email_template_photo_album_custom')[2]
        except ValueError:
            template_id = False
        ctx = dict()
        ctx.update({
            'default_model': 'photo.album.image',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
        })
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }