#-*- coding: utf-8 -*-

from odoo import models, fields, api


class LgpmPurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'
    _description = 'lgpm_purchase.order'

    maintenance_request_ids = fields.One2many(
        comodel_name='maintenance.request',
        inverse_name='purchase_order_id',
        string='Maintenance Request'
    )

    maintenance_request_count = fields.Integer(
        compute='_compute_maintenance_request_count',
        string='# Maintenances'
    )
    @api.depends('maintenance_request_ids')
    def _compute_maintenance_request_count(self):
        for purchase in self:
            purchase.maintenance_request_count = len(purchase.maintenance_request_ids)

    def action_view_maintenance_request(self):
        """This function returns an action that display existing maintenance requests
        of given purchase order ids. When only one found, show the maintenance request
        immediately.
        """
        action = self.env.ref("maintenance.hr_equipment_request_action")
        result = action.read()[0]
        # override the context to get rid of the default filtering on repair order
        result["context"] = {"default_purchase_order_id": self.id}
        maintenance_request_ids = self.mapped("maintenance_request_ids")
        # choose the view_mode accordingly
        if not maintenance_request_ids or len(maintenance_request_ids) > 1:
            result["domain"] = "[('id','in',%s)]" % (maintenance_request_ids.ids)
        elif len(maintenance_request_ids) == 1:
            res = self.env.ref("maintenance.hr_equipment_request_view_form", False)
            form_view = [(res and res.id or False, "form")]
            if "views" in result:
                result["views"] = form_view + [
                    (state, view) for state, view in result["views"] if view != "form"
                ]
            else:
                result["views"] = form_view
            result["res_id"] = maintenance_request_ids.id
        return result