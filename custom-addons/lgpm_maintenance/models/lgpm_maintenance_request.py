#-*- coding: utf-8 -*-

from odoo import models, fields, api


class LgpmMaintenanceRequest(models.Model):
    _name = 'maintenance.request'
    _inherit = ['maintenance.request']
    _description = 'lgpm_maintenance.request'

    """ def maintenance_request_report_button(self):
        return self.env.ref('lgpm_maintenance_request_vg_action_report').report_action(self) """

    equipment_type = fields.Char(
        string='Tipo',
        compute="_compute_equipment_type",
        readonly=True
        )
    owner_name = fields.Char(
        string='Propietario',
        compute="_compute_owner_id",
        readonly=True)
    serial_no = fields.Char(
        string='Número de serie',
        compute="_compute_serial_no",
        readonly=True
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
    def _compute_owner_id(self):
        for maintenance_request in self:
            if maintenance_request.equipment_id:
                maintenance_request.owner_name = self.equipment_id.owner_id.name
            else:
                maintenance_request.owner_name = ''

    @api.depends('equipment_id')
    def _compute_serial_no(self):
        for maintenance_request in self:
            if maintenance_request.equipment_id:
                maintenance_request.serial_no = self.env[
                        'maintenance.equipment'
                        ]._fields[
                            'serial_no'
                        ]
            else:
                maintenance_request.serial_no = ''