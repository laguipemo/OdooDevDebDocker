# -*- coding: utf-8 -*-
# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Photo Albums',
    'license': 'Other proprietary',
    'category': 'Tools',
    'summary': 'Photos / Images Album Manage',
    'price': 39.0,
    'currency': 'EUR',
    'images': ['static/description/image.jpg'],
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/odoo_photo_album_images/131',#'https://youtu.be/Fywh8VAOIRc',
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'www.probuse.com',
    'version': '6.2.3',
    'description': """
Photo Albums
Photo Album
image album
image albums
""",
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'report/report.xml',
        'data/photo_album_template.xml',
        'views/album_tags_view.xml',
        'views/album_type_view.xml',
        'views/photo_album_image_view.xml',
        'views/photo_album_image_line_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
