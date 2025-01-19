#-*- coding: utf-8 -*-

from odoo import models, fields, api


class LgpmMaintenanceEquipment(models.Model):
    _name = 'maintenance.equipment'
    _inherit = ['maintenance.equipment']
    _description = 'lgpm_maintenance.equipment'


    manufacture_date = fields.Date(
        string='Fecha deFabricación',
    )
    equipment_type = fields.Selection(
        string = 'Tipo',
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
    equipment_use = fields.Selection(
        string = 'Tipo de Uso',
        selection=[
            ('NO', ''),
            ('G', 'General'),
            ('AC', 'Ácidos Concentrados'),
        ],
        default='NO',
    )
    inventary_number = fields.Char(
        string='Nº Inventario',
    )
    owner_id = fields.Many2one(
        string='Propietario',
        comodel_name='res.partner',
        ondelete='cascade'
    )
    contact_id = fields.Many2one(
        string='Contacto',
        comodel_name='res.partner',
        ondelete='cascade'
    )
