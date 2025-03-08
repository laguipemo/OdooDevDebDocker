#-*- coding: utf-8 -*-

from odoo import models, fields, api
import os
import base64


class LgpmMaintenanceRequest(models.Model):
    _name = 'maintenance.request'
    _inherit = ['maintenance.request']
    _description = 'lgpm_maintenance.request'

    """ def maintenance_request_report_button(self):
        return self.env.ref('lgpm_maintenance_request_final_action_report').report_action(self) """
    
    VERIFICATION_SELECTION = [
            ('N', ''),
            ('NP', 'NO PROCEDE'),
            ('C', 'CORRECTO'),
            ('F', 'FALTA LEVE'),
            ('RR', 'REQUIERE REPARACIÓN')
        ]

    INTEGRITY_RESULT = [
        ('N', ''),
        ('C', 'CUMPLE'),
        ('NC', 'NO CUMPLE'),
        ('INF', 'INSUFICIENTE')
    ]

    def get_info_about(self, position):
        record_info=self.env['lgpm_maintenance.sat_signatures'].search(
            [('position', '=', position)]
        )
        return (record_info.name, record_info.signature)

    def get_resource_of(self, name):
        record_info=self.env['lgpm_maintenance.sat_report_resources'].search(
            [('name', '=', name)]
        )
        return (record_info.name, record_info.title, record_info.figure)


    def get_default_image(self, image_name):
        image_path = os.path.join(
            os.path.dirname(__file__), '../static/src/img', image_name)
        with open(image_path, 'rb') as image_file:
            base64_image = base64.b64encode(image_file.read())
        return base64_image

    # Mantenance data
    maintenance_date = fields.Date(
        string='Fecha',
        help='Fecha de la realización del mantenimiento'
    )

    # Equipment data
    partner_id = fields.Char(
        string='Fabricante',
        related='equipment_id.partner_id.name'
    )
    manufacture_date = fields.Date(
        string='Fecha de fabricación',
        related='equipment_id.manufacture_date'
    )
    partner_ref = fields.Char(
        string='Referencia',
        related='equipment_id.partner_ref'
    )
    lot_id = fields.Char(
        string='Número de serie',
        related='equipment_id.lot_id.name'
        )
    equipment_type = fields.Char(
        string='Tipo',
        compute='_compute_equipment_type'
    )
    equipment_use = fields.Char(
        string='Tipo de Uso',
        compute='_compute_equipment_use'
    )
    inventary_number = fields.Char(
        string='Nº Inventario',
        related='equipment_id.inventary_number'
    )

    # Owner and contact data
    owner_name = fields.Char(
        string='Propietario',
        related='equipment_id.owner_id.name'
    )
    contact_name = fields.Char(
        string='Contacto',
        related='equipment_id.contact_id.name'
    )
    contact_email = fields.Char(
        string='Correo',
        related='equipment_id.contact_id.email'
    )
    contact_phone = fields.Char(
        string='Teléfono',
        related='equipment_id.contact_id.phone'
    )


    # General verification parameters
    sat_is_working = fields.Boolean(
        string='¿El equipo está funcionando?',
        help='Indica si el equipo está funcionando'
    )
    sat_equipment_stability = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='NP',
        string='Estabilidad del equipo'
    )
    sat_glass_wiring_state = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Estado cristales y cableado'
    )
    sat_operating_hours = fields.Integer(
        string='Horas de funcionamiento',
        help='Horas de funcionamiento del equipo'
    )

    sat_digital_ctrl = fields.Selection(
        string='Control digital',
        selection=VERIFICATION_SELECTION,
        default='N'
    )
    sat_extraction_sys = fields.Selection(
        string='Sistema de extracción',
        selection=VERIFICATION_SELECTION,
        default='N'
    )
    sat_var_speed = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='NP',
        string='Posición variador'
    )
    # Equipment special requirements
    requirements_partner = fields.Text(
        string='Requerimientos fabricante',
        help='Requerimientos del fabricante'
    )
    requirements_client = fields.Text(
        string='Requerimientos cliente',
        help='Requerimientos del cliente'
    )

    # Verification and adjustments of components and medias
    sat_visual_acustic_ctrls = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Controles visuales y acústicos'
    )
    sat_temp_alarm = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Alarma de temperatura'
    )
    sat_surface_protection = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Protección de la superficie'
    )
    sat_fixed_parts = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Sujeción partes fijas'
    )
    sat_insulation_joints = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Aislamiento de juntas'
    )
    sat_faucets_function = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Estado grifos'
    )
    sat_manoreductors_function = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Estado manoreductores'
    )
    sat_presence_ctrl = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='NP',
        string='Control de presencia'
    )
    sat_autoprotec = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='NP',
        string='Autoprotec'
    )

    sat_alarm_trigger = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Disparo de la alarma'
    )
    sat_guillotine_function = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Funcionamiento guillotina'
    )
    sat_guillotine_gnrl_state = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Estado general guillotina'
    )
    sat_guillotine_v_force = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='NP',
        string='Fuerza vertical guillotina'
    )
    sat_airflow_sensors = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Sensores flujo de aire'
    )
    sat_airflow_direction = fields.Boolean(
        string='¿La dirección del flujo de aire es correcta?',
        help='Indica si la dirección del flujo de aire es correcta'
    )
    sat_airflow_uniformity = fields.Boolean(
        string='¿El flujo de aire es uniforme?',
        help='Es uniforme si no hay turbulencias o zonas muertas en el flujo de aire'
    )
    sat_filters_state = fields.Selection(
        selection=VERIFICATION_SELECTION,
        default='N',
        string='Montaje de filtros'
    )
    

    # Parameters to measure
    work_length = fields.Integer(
        string='Longitud de trabajo',
        help='Longitud de trabajo del equipo en mm'
    )
    work_length_m = fields.Float(
        compute='_compute_work_length_m',
    )
    work_height = fields.Integer(
        string='Altura de trabajo',
        help='Atura de trabajo para a gillotina en mm'
    )
    work_height_m = fields.Float(
        compute='_compute_work_height_m'
    )
    measurement_area = fields.Float(
        string='Superficie de medición',
        compute='_compute_measurement_area',
        store=True,
        help='Superficie de medición en metros cuadrados'
    )

    frontal_v1 = fields.Float(
        default=0.0
    )
    frontal_v2 = fields.Float(
        default=0.0
    )
    frontal_v3 = fields.Float(
        default=0.0
    )
    frontal_v4 = fields.Float(
        default=0.0
    )
    frontal_v5 = fields.Float(
        default=0.0
    )
    frontal_v6 = fields.Float(
        default=0.0
    )
    frontal_v7 = fields.Float(
        default=0.0
    )
    frontal_v8 = fields.Float(
        default=0.0
    )
    frontal_v9 = fields.Float(
        default=0.0
    )
    frontal_v_media = fields.Float(
        compute='_compute_frontal_v_media'
    )
    extraction_volume = fields.Float(
        string='Volumen de extracción',
        compute='_compute_extraction_volume'
    )

    # Only CF filter integrity, etc
    filter1_number = fields.Char()
    filter2_number = fields.Char()
    filter3_number = fields.Char()
    filter1_serial_id = fields.Char()
    filter2_serial_id = fields.Char()
    filter3_serial_id = fields.Char()
    filter1_dimensions = fields.Char()
    filter2_dimensions = fields.Char()
    filter3_dimensions = fields.Char()
    aerosol1_conc = fields.Float(
        default=0.0
    )
    aerosol2_conc = fields.Float(
        default=0.0
    )
    aerosol3_conc = fields.Float(
        default=0.0
    )
    integrity1_value = fields.Float(
        default=0.0
    )
    integrity2_value = fields.Float(
        default=0.0
    )
    integrity3_value = fields.Float(
        default=0.0
    )
    integrity1_result = fields.Selection(
        selection=INTEGRITY_RESULT,
        default='N'
    )
    integrity2_result = fields.Selection(
        selection=INTEGRITY_RESULT,
        default='N'
    )
    integrity3_result = fields.Selection(
        selection=INTEGRITY_RESULT,
        default='N'
    )
    
    # Only CF paramaters to measure
    diff_press = fields.Float(
        string='Presión diferencial',
        default=0.0
    )
    temperature = fields.Float(
        string='Temperatura',
        default=0.0
    )
    # Only if guillotine vertical is not N or NP
    guillotine_force = fields.Float(
        string='Valor fuerza guillotina',
        default=0.0
    )
    
    lighting_v1 = fields.Float(
        default=0.0
    )
    lighting_v2 = fields.Float(
        default=0.0
    )
    lighting_v3 = fields.Float(
        default=0.0
    )
    lighting_v_media = fields.Float(
        compute='_compute_lighting_v_media'
    )
    noise_level = fields.Float(
        string='Sonido',
        default=0.0
    )

    # Related info ONLY for internal equipment
    purchase_order_id = fields.Many2one(
        string='Orden de compra',
        comodel_name='purchase.order', 
        ondelete='cascade'
    )
    
    # Observations and final considerations
    observations = fields.Html(
        string="Observaciones"
    )
    non_conformities = fields.Html(
        string="No conformidades"
    )
    complies_regulation = fields.Boolean(
        string="El equipo está de acuerdo con las normas / regulaciones petinentes"
    )
    needs_intervention = fields.Boolean(
        string="Por cuestiones de seguridad es necesaria la intervención del equipo"
    )

    # Photos
    photo1 = fields.Image(
        max_width=200,
        max_height=200
    )
    photo2 = fields.Image(
        max_width=200,
        max_height=200
    )
    photo3 = fields.Image(
        max_width=200,
        max_height=200
    )
    photo4 = fields.Image(
        max_width=200,
        max_height=200
    )
    photo5 = fields.Image(
        max_width=200,
        max_height=200
    )
    photo6 = fields.Image(
        max_width=200,
        max_height=200
    )

    # Methods to compute fields and

    @api.depends('equipment_id')
    def _compute_equipment_type(self):
        for maintenance_request in self:
            if maintenance_request.equipment_id:
                key = maintenance_request.equipment_id.equipment_type
                maintenance_request.equipment_type = dict(
                    self.env[
                        'maintenance.equipment'
                        ]._fields[
                            'equipment_type'
                            ].selection).get(key)
            else:
                maintenance_request.equipment_type = ''

    @api.depends('equipment_id')
    def _compute_equipment_use(self):
        for maintenance_request in self:
            if maintenance_request.equipment_id:
                key = maintenance_request.equipment_id.equipment_use
                maintenance_request.equipment_use = dict(
                    self.env[
                        'maintenance.equipment'
                        ]._fields[
                            'equipment_use'
                            ].selection).get(key)
            else:
                maintenance_request.equipment_use = ''

    @api.depends('work_length', 'work_height')
    def _compute_measurement_area(self):
        for maintenance_request in self:
            if maintenance_request.equipment_type.lower() in ['vitrina de gases', 'cabina de flujo', 'cabina de pesadas']:
                maintenance_request.measurement_area = (
                    (maintenance_request.work_length/1000) * (maintenance_request.work_height/1000)
                )
            else:
                maintenance_request.measurement_area = 0.0

    @api.depends(
        'frontal_v1',
        'frontal_v2',
        'frontal_v3',
        'frontal_v4',
        'frontal_v5',
        'frontal_v6',
        'frontal_v7',
        'frontal_v8',
        'frontal_v9',
        )
    def _compute_frontal_v_media(self):
        for maintenance_request in self:
            if maintenance_request.equipment_type.lower() in ['vitrina de gases', 'cabina de flujo', 'cabina de pesadas']:
                values = [
                    maintenance_request.frontal_v1,
                    maintenance_request.frontal_v2,
                    maintenance_request.frontal_v3,
                    maintenance_request.frontal_v4,
                    maintenance_request.frontal_v5,
                    maintenance_request.frontal_v6,
                    maintenance_request.frontal_v7,
                    maintenance_request.frontal_v8,
                    maintenance_request.frontal_v9
                ]
            else:
                values = [
                    maintenance_request.frontal_v1,
                    maintenance_request.frontal_v2,
                    maintenance_request.frontal_v3
                ]
            maintenance_request.frontal_v_media = sum(values)/len(values)

    @api.depends('frontal_v_media', 'measurement_area')
    def _compute_extraction_volume(self):
        for maintenance_request in self:
            maintenance_request.extraction_volume = maintenance_request.measurement_area * maintenance_request.frontal_v_media * 3600
    
    @api.depends(
        'lighting_v1',
        'lighting_v2',
        'lighting_v3',
        )
    def _compute_lighting_v_media(self):
        for maintenance_request in self:
            values = [
                maintenance_request.lighting_v1,
                maintenance_request.lighting_v2,
                maintenance_request.lighting_v3
            ]
            maintenance_request.lighting_v_media = sum(values)/len(values)


    def convert_to_meters(self, value):
        return value/1000.0

    @api.depends('work_length')
    def _compute_work_length_m(self):
        for maintenance_request in self:
            maintenance_request.work_length_m = self.convert_to_meters(maintenance_request.work_length)

    @api.depends('work_height')
    def _compute_work_height_m(self):
        for maintenance_request in self:
            maintenance_request.work_height_m = self.convert_to_meters(maintenance_request.work_height)
