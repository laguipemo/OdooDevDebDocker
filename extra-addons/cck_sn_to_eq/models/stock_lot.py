from odoo import fields, models


class StockLot(models.Model):
    _inherit = 'stock.lot'

    product_tracking = fields.Selection(related='product_id.tracking')

    def action_open_eq(self):
        """
        :return: Open related record or Create new record
        """
        eq = self.env['maintenance.equipment'].search([('lot_id', '=', self.id)])

        action = self.env['ir.actions.act_window']._for_xml_id('maintenance.hr_equipment_action')
        action['view_mode'] = 'form'
        action['views'] = [(False, 'form')]
        action['target'] = 'new'
        if eq:
            action['res_id'] = eq.id
        else:
            action['context'] = {
                'default_name': self.product_id.name,
                'default_serial_no': self.ref or self.name,
                'default_note': self.note,
                'default_effective_date': self.create_date,
                'default_location': self.quant_ids.filtered(lambda q: q.location_id.usage == 'internal' and q.quantity > 0).location_id.display_name or '',
                'default_lot_id': self.id,
            }
        return action
