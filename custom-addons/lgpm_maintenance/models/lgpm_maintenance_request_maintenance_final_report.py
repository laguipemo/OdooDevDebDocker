from odoo import models, fields, api

class LgpmMaintenanceRequestMaintenanceFinalReport(models.AbstractModel):
    _name = 'report.lgpm_maintenance.request_maintenance_final_report'
    _description = 'report.lgpm_maintenance.request_maintenance_final_report'

    def _get_report_values(self, docids, data=None):
        # get the report action back as we will need its data
        report = self.env['ir.actions.report']._get_report_from_name('lgpm_maintenance.request_maintenance_final_report')
        # get the records selected for this rendering of the report
        docs = self.env[report.model].browse(docids)
        # return a custom rendering context
        return {
            'doc_ids': docids,
            'doc_model': 'maintenance.request',
            'docs': docs,
            'data': data,
        }
    