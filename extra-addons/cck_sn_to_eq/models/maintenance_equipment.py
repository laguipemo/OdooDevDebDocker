from odoo import fields, models


class StockLot(models.Model):
    _inherit = 'maintenance.equipment'

    lot_id = fields.Many2one('stock.lot')

    _sql_constraints = [
        ('lot_uniq', 'unique (lot_id)', 'The related Serial number of the equipment must be unique !')
    ]
