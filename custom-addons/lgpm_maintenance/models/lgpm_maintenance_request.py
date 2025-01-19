#-*- coding: utf-8 -*-

from odoo import models, fields, api


class LgpmMaintenanceRequest(models.Model):
    _name = 'maintenance.request'
    _inherit = ['maintenance.request']
    _description = 'lgpm_maintenance.request'

    """ def maintenance_request_report_button(self):
        return self.env.ref('lgpm_maintenance_request_vg_action_report').report_action(self) """

    maintenance_date = fields.Date(
        string='Fecha',
        help='Fecha de la realización del mantenimiento',
        required=True
    )
    manufacture_date = fields.Date(
        string='Fecha de fabricación',
        related='equipment_id.manufacture_date'
    )
    equipment_type = fields.Char(
        string='Tipo',
        compute='_compute_equipment_type'
    )
    equipment_use = fields.Char(
        string='Tipo de Uso',
        compute='_compute_equipment_use'
    )
    owner_name = fields.Char(
        string='Propietario',
        related='equipment_id.owner_id.name'
        )
    lot_id = fields.Char(
        string='Número de serie',
        related='equipment_id.lot_id.name'
        )
    inventary_number = fields.Char(
        string='Nº Inventario',
        related='equipment_id.inventary_number'
    )
    contact_name = fields.Char(
        string='Contacto',
        related='equipment_id.contact_id.name'
        )
    contact_email = fields.Char(
        string='Correo',
        related='equipment_id.contact_id.email'
        )
    contact_phone = fields.Char(
        string='Teléfono',
        related='equipment_id.contact_id.phone'
        )
    partner_id = fields.Char(
        string='Fabricante',
        related='equipment_id.partner_id.name'
    )
    partner_ref = fields.Char(
        string='Referencia',
        related='equipment_id.partner_ref'
    )
    

    purchase_order_id = fields.Many2one(
        string='Orden de compra',
        comodel_name='purchase.order', 
        ondelete='cascade'
        )

    @api.depends('equipment_id')
    def _compute_equipment_type(self):
        for maintenance_request in self:
            if maintenance_request.equipment_id:
                key = self.equipment_id.equipment_type
                maintenance_request.equipment_type = dict(
                    self.env[
                        'maintenance.equipment'
                        ]._fields[
                            'equipment_type'
                            ].selection).get(key)
            else:
                maintenance_request.equipment_type = ''

    @api.depends('equipment_id')
    def _compute_equipment_use(self):
        for maintenance_request in self:
            if maintenance_request.equipment_id:
                key = self.equipment_id.equipment_use
                maintenance_request.equipment_use = dict(
                    self.env[
                        'maintenance.equipment'
                        ]._fields[
                            'equipment_use'
                            ].selection).get(key)
            else:
                maintenance_request.equipment_use = ''