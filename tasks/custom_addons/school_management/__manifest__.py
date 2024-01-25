# -*- coding: utf-8 -*--
{
    'name': "School Management",
    'summary': """School Management Software""",

    'description': """
    Treating Schools
    """,

    'author': "My Company",
    'website': "http://www.your.com",
    'category': 'Tools',
    'version': '16.0.1.0.0',
    'depends': ['base', 'contacts', 'hr', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/school.xml',
    ],

    'demo': [
    ],
    'images': ['ststic/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False
}