#-*- coding: utf-8 -*-

from odoo import models, fields, api


class LgpmMaintenanceRequest(models.Model):
    _name = 'maintenance.request'
    _inherit = ['maintenance.request']
    _description = 'lgpm_maintenance.request'

    equipment_type = fields.Char(string='Type', compute="_compute_equipment_type", readonly=True)

    @api.depends('equipment_id')
    def _compute_equipment_type(self):
        for maintenance_request in self:
            if maintenance_request.equipment_id:
                maintenance_request.equipment_type = self.equipment_id.equipment_type    
            else: 
                maintenance_request.equipment_type = ''