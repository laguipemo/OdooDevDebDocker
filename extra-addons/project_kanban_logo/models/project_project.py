from odoo import models, fields


class ProjectProjectInherit(models.Model):
    _inherit = 'project.project'

    image = fields.Binary(string='Company Logo')