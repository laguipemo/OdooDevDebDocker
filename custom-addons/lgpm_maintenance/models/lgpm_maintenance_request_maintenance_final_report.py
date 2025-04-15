from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class LgpmMaintenanceRequestMaintenanceFinalReport(models.AbstractModel):
    _name = 'report.lgpm_maintenance.request_maintenance_final_report'
    _description = 'report.lgpm_maintenance.request_maintenance_final_report'

    def _get_report_values(self, docids, data=None):
        # get the report action back as we will need its data
        report = self.env['ir.actions.report']._get_report_from_name('lgpm_maintenance.request_maintenance_final_report')
        # get the records selected for this rendering of the report
        docs = self.env[report.model].browse(docids)

        # raise an error if user select more than one type of equipment
        equipment_types = set(docs.mapped('equipment_id.equipment_type'))
        if len(equipment_types) > 1:
            if equipment_types != {'VG', 'CA'}:
                _logger.info(equipment_types)
                raise UserError(_('Solo se puede seleccionar mantenimientos del mismo tipo de equipo'))
            
        # return a custom rendering context
        return {
            'doc_ids': docids,
            'doc_model': 'maintenance.request',
            'docs': docs,
            'data': data,
        }
    