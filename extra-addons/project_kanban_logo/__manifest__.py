# -*- coding: utf-8 -*-
{
    'name': "Project Logo",

    'summary': """
        Add company logo in project Kanban view""",

    'description': """
        
    """,

    'author': "Odolution",
    'category': 'Project',
    'version': '16.1',
    'depends': ['project'],
    'license': 'OPL-1',
    'data': [
        'views/project_project.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'project_kanban_logo/static/src/scss/project.scss',
        ],
    },
    'images': ['static/description/images/1.PNG'],
    'demo': [
    ],
}
