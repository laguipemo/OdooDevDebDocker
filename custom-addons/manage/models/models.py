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


class bug(models.Model):
    _name = "manage.bug"
    _description = "manage.bug"
    _inherit = "manage.task"

    technologies = fields.Many2many(comodel_name="manage.technology",
                                    string="Tecnologías",
                                    relation="bug_technology_rel",
                                    column1="bug_id",
                                    column2="technology_id",
                                    help='Tecnologías utilizadas en el bug')
    tasks_linked = fields.Many2many(comodel_name="manage.task",
                                    string="Tareas",
                                    relation="bug_task_rel",
                                    column1="bug_id",
                                    column2="task_id",
                                    help='Tareas relacionadas con el bug')
    bugs_linked = fields.Many2many(comodel_name="manage.bug",
                                   string="Bugs",
                                   relation="bug_bug_rel",
                                   column1="bug_id",
                                   column2="bug_id",
                                   help='Bugs relacionados con el bug')
    improvements_linked = fields.Many2many(comodel_name="manage.improvement",
                                           string="Mejoras",
                                           relation="bug_improvement_rel",
                                           column1="bug_id",
                                           column2="improvement_id",
                                           help='Mejoras relacionadas con el bug')
    developers = fields.Many2many(comodel_name="res.partner",
                                    string="Desarrolladores",
                                    relation="bug_developer_rel",
                                    column1="bug_id",
                                    column2="developer_id",
                                    help='Desarrolladores involucrados en el bug')


class improvement(models.Model):
    _name = 'manage.improvement'
    _description = 'manage.improvement'
    _inherit = "manage.task"

    technologies = fields.Many2many(comodel_name="manage.technology",
                                    string="Tecnologías",
                                    relation="improvement_technology_rel",
                                    column1="improvement_id",
                                    column2="technology_id",
                                    help='Tecnologías utilizadas en la mejora')
    histories_linked = fields.Many2many(comodel_name="manage.history",
                                        string="Historias",
                                        relation="improvement_history_rel",
                                        column1="improvement_id",
                                        column2="history_id",
                                        help='Historias relacionadas con la mejora')
    developers = fields.Many2many(comodel_name="res.partner",
                                    string="Desarrolladores",
                                    relation="improvement_developer_rel",
                                    column1="improvement_id",
                                    column2="developer_id",
                                    help='Desarrolladores involucrados en la mejora')  
    

class developer(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
    is_developer = fields.Boolean()
    technologies = fields.Many2many(comodel_name="manage.technology", 
                                    string="Tecnologías", 
                                    relation="developer_technology_rel", 
                                    column1="developer_id", 
                                    column2="technology_id",
                                    help='Tecnologías utilizadas por el desarrollador')
    
    @api.onchange("is_developer")
    def _onchange_is_developer(self):
        categories = self.env["res.partner.category"].search([('name', '=', "Developer")])
        if len(categories) > 0:
            category = categories[0]
        else:
            category = self.env["res.partner.category"].create({"name": "Developer"})
        self.category_id = [(4, category.id)]

class project(models.Model):
    _name = 'manage.project'
    _description = 'manage.project'

    name = fields.Char()
    description = fields.Text()
    histories = fields.One2many(comodel_name="manage.history", 
                                inverse_name="project", 
                                string="Historial",
                                help='Historial de usuarios asociados al proyecto')
    sprints = fields.One2many(comodel_name="manage.sprint", 
                              inverse_name="project", 
                              string="Sprints",
                              help='Sprints asociados al proyecto')

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
    tasks = fields.One2many(comodel_name="manage.task", 
                            inverse_name="history", 
                            string="Tareas", 
                            help='Tareas relacionadas')
    used_technologies = fields.Many2many(comodel_name="manage.technology",
                                         compute="_compute_used_technologies",
                                         string="Tecnologias utilizadas",
                                         help='Tecnologias utilizadas en la historia')

    def _compute_used_technologies(self):
        for history in self:
            technologies = None
            for task in history.tasks:
                if task.technologies:
                    if technologies:
                        technologies += task.technologies
                    else:
                        technologies = task.technologies
            history.used_technologies = technologies
            

class task(models.Model):
    _name = 'manage.task'
    _description = 'manage.task'

    project = fields.Many2one(comodel_name="manage.project", 
                              related='history.project', 
                              readonly=True,
                              string="Proyecto", 
                              help='Proyecto relacionado')
    code = fields.Char(compute="_compute_code")
    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre")
    history = fields.Many2one(comodel_name="manage.history", 
                              ondelete="cascade", 
                              string="Historial", 
                              help='Historial relacionado')
    description = fields.Text()
    definition_date = fields.Datetime(default=lambda d: datetime.datetime.now(), 
                                      string="Fecha de definición", 
                                      help='Fecha de definición de la tarea')
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()
    sprint = fields.Many2one(comodel_name="manage.sprint", 
                             compute="_compute_sprint", 
                             string="Sprint", 
                             help='Sprint relacionado')
    developer = fields.Many2many(comodel_name="res.partner", 
                                 relation="manage_task_developer_rel", 
                                 column1="task_id", 
                                 column2="developer_id", 
                                 string="Desarrolladores", 
                                 help='Desarrolladores relacionados')
    technologies = fields.Many2many(comodel_name="manage.technology", 
                                    relation="manage_task_technology_rel",
                                    column1="task_id", 
                                    column2="technology_id", 
                                    string="Tecnologias", 
                                    help='Tecnologias relacionadas')


    
    def _compute_code(self): # self siempre es una colección de registros que hay que recorrer
        for task in self:
            try:
                #task.code = "TSK_{}".format(task.id_) # Ej: fuerzo error al utilizar un campo que no existe
                task.code = "TSK_{}".format(task.id)
                _logger.debug("Generado código de tarea: {}".format(task.code))
            except:
                raise ValidationError(_("No se puede calcular el código de la tarea"))

    @api.depends("code", "start_date")
    def _compute_sprint(self):
        for task in self:
            # buscar los sprints correspondientes al proyecto de la historia de usuario en la que está la tarea
            list_sprints_project = self.env["manage.sprint"].search([("project.id","=", task.history.project.id)])
            # obtener el sprint activo. Estamos asumiendo que solo hay un sprint activo por proyecto
            found = False
            for sprint in list_sprints_project:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    if isinstance(task.start_date, datetime.datetime) and sprint.end_date > task.start_date:
                        task.sprint = sprint
                        found = True
                        break
            if not found:
                task.sprint = False

    
class sprint(models.Model):
    _name = 'manage.sprint'
    _description = 'manage.sprint'

    project = fields.Many2one(comodel_name="manage.project", 
                              ondelete="cascade", 
                              string="Proyecto", 
                              help='Proyecto relacionado')
    name = fields.Char()
    description = fields.Text()
    start_date = fields.Datetime()
    duration = fields.Integer(default=15, string="Duración (días)", help='Duración del sprint en días')
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
