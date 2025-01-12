#-*- coding: utf-8 -*-

from odoo import models, fields, api


class LgpmMaintenanceEquipment(models.Model):
    _name = 'maintenance.equipment'
    _inherit = ['maintenance.equipment']
    _description = 'lgpm_maintenance.equipment'

    equipment_type = fields.Selection(
        string = 'Type',
        selection=[
            ('VG', 'Vitrina de Gases'),
            ('CF', 'Cabina de Flujo'),
            ('PALP', 'Punto de Aspiración Localizada Pared'),
            ('PALB', 'Punto de Aspiración Localizada Brazo'),
            ('AS', 'Armario de seguridad'),
            ('NO', ''),
        ],
        default='NO'
    )
