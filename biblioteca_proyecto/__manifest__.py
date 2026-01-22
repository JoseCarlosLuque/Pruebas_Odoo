{
    'name': "biblioteca_proyecto",

    'summary': "Proyecto Biblioteca en Odoo para aprender desarrollo de módulos",

    'description': """
    Módulo de gestión de una biblioteca que permite administrar libros, autores y préstamos. Incluye funcionalidades para registrar nuevos libros, gestionar su estado (disponible, prestado, dañado, perdido) y almacenar información relevante como ISBN, fecha de publicación y número de páginas.

    Estoy siguiendo el curso de Odoo Next y esto es parte del proyecto final para practicar el desarrollo. 
    """,

    'author': "Biblioteca Proyecto",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/menu_view.xml',
        'views/usuario_view.xml',
        'demo/demo_usuarios.xml',
        'demo/demo.xml', 
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',   
    ],
}

