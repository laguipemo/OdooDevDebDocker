# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo import _
import datetime
import logging


_logger = logging.getLogger(__name__) # descriptor del fichero utilizado como log

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


class project(models.Model):
    _name = 'manage.project'
    _description = 'manage.project'

    name = fields.Char()
    description = fields.Text()
    histories = fields.One2many(comodel_name="manage.history", 
                                inverse_name="project", 
                                string="Historial",
                                help='Historial de usuarios asociados al proyecto')

class history(models.Model):
    _name = 'manage.history'
    _description = 'manage.history'

    name = fields.Char()
    description = fields.Text()
    #muchas historias está asociadas a un proyecto 
    project = fields.Many2one(comodel_name="manage.project", 
                              ondelete="cascade", 
                              string="Proyecto", 
                              help='Proyecto relacionado')

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
            try:
                if len(task.sprint) == 0:  # no contamos con un sprint
                    #task.code = "TSK_{}".format(task.id_) # fuerzo error al utilizar un campo que no existe
                    task.code = "TSK_{}".format(task.id)
                else:
                    task.code = "{}_{}".format(task.sprint.name.upper(), task.id)
                
                _logger.debug("Generado código de tarea: {}".format(task.code))
            except:
                raise ValidationError(_("No se puede calcular el código de la tarea"))
    
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
            if sprint.duration > 0 and isinstance(sprint.start_date, datetime.datetime):
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date

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
