# -*- coding: utf-8 -*-
{
    'name': "lgpm_maintenance",

    'summary': """
        Extends the maintenance module with SAT verifications""",

    'description': """
        The module extends the base maintenance module with SAT verifications data performed on gas extraction equipments
    """,

    'author': "LGPM developments",
    'website': "https://github.com/laguipemo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'maintenance', 'purchase', 'cck_sn_to_eq'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/lgpm_maintenance_equipment_views.xml',
        'views/lgpm_maintenance_request_views.xml',
        'views/lgpm_maintenance_request_purchase_views.xml',
        'views/lgpm_maintenance_sat_signatures_views.xml',
        'views/lgpm_maintenance_sat_report_resources_views.xml',
        'reports/template_anexo_a_content_report.xml',
        'reports/template_anexo_b_content_report.xml',
        'reports/template_anexo_b_content_vg_report.xml',
        'reports/template_anexo_b_content_cf_report.xml',
        'reports/template_anexo_b_content_as_report.xml',
        'reports/template_anexo_b_content_palb_report.xml',
        'reports/template_anexo_c_content_report.xml',
        'reports/template_anexo_d_content_report.xml',
        'reports/template_anexo_g_content_report.xml',
        'reports/template_title_page_of_anexos_report.xml',
        'reports/template_theoretical_intro_vg_report.xml',
        'reports/template_theoretical_intro_cf_report.xml',
        'reports/template_theoretical_intro_as_report.xml',
        'reports/template_theoretical_intro_palb_report.xml',
        'reports/lgpm_maintenance_final_report.xml',
        'reports/lgpm_maintenance_data_report.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
