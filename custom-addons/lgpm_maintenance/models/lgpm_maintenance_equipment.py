#-*- coding: utf-8 -*-

from odoo import models, fields, api


class LgpmMaintenanceEquipment(models.Model):
    _name = 'maintenance.equipment'
    _inherit = ['maintenance.equipment']
    _description = 'lgpm_maintenance.equipment'


    manufacture_date = fields.Date(
        string='Año de Fabricación',
    )
    equipment_type = fields.Selection(
        string = 'Tipo',
        selection=[
            ('NO', ''),
            ('AS', 'Armario de Seguridad'),
            ('CF', 'Cabina de Flujo'),
            ('CP', 'Cabina de Pesadas'),
            ('CA', 'Capotaje'),
            ('PALP', 'Punto de Aspiración Localizada Pared'),
            ('PALB', 'Punto de Aspiración Localizada Brazo'),
            ('VG', 'Vitrina de Gases'),
        ],
        default='NO'
    )
    vg_type_use = fields.Selection(
        string = 'Tipo de vitrina',
        selection=[
            ('NO', ''),
            ('G', 'Uso General'),
            ('AC', 'Ácidos Concentrados'),
            ('W', 'Walk-in'),
        ],
        default='NO',
    )
    ca_type_use = fields.Selection(
        string = 'Tipo de Capotaje',
        selection=[
            ('NO', ''),
            ('G', 'Uso General'),
            ('AC', 'Ácidos Concentrados'),
            ('W', 'Walk-in'),
        ],
        default='NO',
    )
    cf_type_use = fields.Selection(
        string = 'Tipo de Cabina',
        selection=[
            ('NO', ''),
            ('QG', 'Flujo Laminar'),
            ('SB', 'Seguridad Biológica')
        ],
        default='NO'
    )
    cp_type_use = fields.Selection(
        string = 'Tipo de Uso',
        selection=[
            ('NO', ''),
            ('G', 'Uso General'),
            ('SP','Uso Especial')
        ],
        default='NO'
    )
    as_type_use = fields.Selection(
        string= 'Tipo de armario',
        selection=[
            ('NO', ''),
            ('QG', 'Químicos Generales'),
            ('INFL', 'Inflamables'),
            ('BG', 'Bombonas de Gas'),
            ('AB', 'Ácidos y Bases')
        ],
        default='NO'
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
