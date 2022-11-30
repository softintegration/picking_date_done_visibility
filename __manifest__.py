# -*- coding: utf-8 -*-

{
    'name': 'picking date done visibility settings',
    'version': '1.0.1.1',
    'author':'Soft-integration',
    'category': 'Sales',
    'summary': 'Configure the visibility of picking date done',
    'description': "",
    'depends': [
        'stock',
    ],
    'data': [
        'security/picking_date_done_visibility_security.xml',
        'views/stock_picking_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
