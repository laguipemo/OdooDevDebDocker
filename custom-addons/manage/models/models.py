# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


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

    code = fields.Char(compute="_compute_code")
    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Text()
    creation_date = fields.Date()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()
    sprint = fields.Many2one(comodel_name="manage.sprint", ondelete="cascade", string="Sprint", help='Sprint relacionado')
    technologies = fields.Many2many(comodel_name="manage.technology", 
                                    relation="manage_task_technology_rel",
                                    column1="task_id", 
                                    column2="technology_id", 
                                    string="Tecnologias", 
                                    help='Tecnologias relacionadas')
    
    def _compute_code(self): # self siempre es una colección de registros que hay que recorrer
        for task in self:
            if len(task.sprint) == 0:  # no contamos con un sprint
                task.code = "TSK_{}".format(task.id)
            else:
                task.code = "{}_{}".format(task.sprint.name.upper(), task.id)
    
class sprint(models.Model):
    _name = 'manage.sprint'
    _description = 'manage.sprint'

    name = fields.Char()
    description = fields.Text()
    start_date = fields.Datetime()
    duration = fields.Integer(string="Duración (días)")
    end_date = fields.Datetime(compute="_compute_end_date", store=True)
    tasks = fields.One2many(comodel_name="manage.task", inverse_name="sprint", string="Tareas")

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for sprint in self:
            if sprint.duration:
                if not sprint.start_date:
                    sprint.start_date = datetime.now()
                sprint.end_date = sprint.start_date + timedelta(days=sprint.duration)

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
