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
    'depends': ['base', 'maintenance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/lgpm_maintenance_equipment_views.xml',
        'views/lgpm_maintenance_request_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
