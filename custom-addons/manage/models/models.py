# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class manage(models.Model):
#     _name = 'manage.manage'
#     _description = 'manage.manage'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class task(models.Model):
    _name = 'manage.task'
    _description = 'manage.task'

    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Text()
    creation_date = fields.Date()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()
    sprint = fields.Many2one(comodel_name="manage.sprint", string="Sprint", help='Sprint relacionado')
    technologies = fields.Many2many(comodel_name="manage.technology", 
                                    relation="manage_task_technology_rel",
                                    column1="task_id", 
                                    column2="technology_id", 
                                    string="Tecnologias", 
                                    help='Tecnologias relacionadas')
    
class sprint(models.Model):
    _name = 'manage.sprint'
    _description = 'manage.sprint'

    name = fields.Char()
    description = fields.Text()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    tasks = fields.One2many(comodel_name="manage.task", inverse_name="sprint", string="Tareas")

class technology(models.Model):
    _name = 'manage.technology'
    _description = 'manage.technology'

    name = fields.Char()
    description = fields.Text()
    photo = fields.Image(max_width=200, max_height=200) #fields.Binary()
    tasks = fields.Many2many(comodel_name="manage.task", 
                             relation="manage_task_technology_rel", 
                             column1="technology_id", 
                             column2="task_id",
                             string="Tareas",
                             help='Tareas relacionadas')
