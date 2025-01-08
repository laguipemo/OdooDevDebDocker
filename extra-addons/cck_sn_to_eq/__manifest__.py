# Copyright 2023 Cck020025 (<https://github.com/cck020025>)
{
    "name": "Create Maintenance Equipment by SN",
    'author': 'Cck020025',
    'website': 'https://github.com/cck020025',
    'version': '1.0.1',
    'category': 'Inventory',
    'license': 'LGPL-3',
    'description': '''Auto fill name, serial number, note and used in location''',
    'depends': ['stock', 'maintenance'],
    'data': [
        'views/stock_lot.xml',
        'views/maintenance_equipment.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [
        'static/description/main.png'
    ]
}
