# -*- coding: utf-8 -*-
{
    'name': "Partner Business ID",

    'summary': """Support for Finnish business ids (y-tunnus)""",

    'description': """
        This module adds support for Finnish business ids (y-tunnus).
	    The id can be generated automatically from company's TIL field, or it can be set manually.
    """,

    'author': "Mikko Närjänen",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
