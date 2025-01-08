{
    'name': 'Product Multiple Images Upload',
    'author': 'Opsway',
    'version': '16.0.1.0',
    'website': 'https://www.opsway.com',
    'category': 'Sales',
    'description': 'Module to upload multiple images for a product',
    'summary': """
        Module to upload multiple images for a product
    """,
    'depends': [
        'web',
        'website_sale',
    ],
    'data': [
        'views/view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'product_multiple_images_upload/static/src/*.js',
            'product_multiple_images_upload/static/src/*.scss',
            'product_multiple_images_upload/static/src/*.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
