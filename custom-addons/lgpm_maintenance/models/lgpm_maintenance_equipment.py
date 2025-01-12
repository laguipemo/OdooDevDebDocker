#-*- coding: utf-8 -*-

from odoo import models, fields, api


class LgpmMaintenanceEquipment(models.Model):
    _name = 'maintenance.equipment'
    _inherit = ['maintenance.equipment']
    _description = 'lgpm_maintenance.equipment'

    equipment_type = fields.Selection(
        string = 'Type',
        selection=[
            ('NO', ''),
            ('AS', 'Armario de Seguridad'),
            ('CF', 'Cabina de Flujo'),
            ('CP', 'Cabina de Pesadas'),
            ('PALP', 'Punto de Aspiración Localizada Pared'),
            ('PALB', 'Punto de Aspiración Localizada Brazo'),
            ('VG', 'Vitrina de Gases'),
        ],
        default='NO'
    )
