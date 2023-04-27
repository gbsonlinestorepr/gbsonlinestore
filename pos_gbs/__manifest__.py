# -*- coding: utf-8 -*-
{
    'name': 'Point Of Sale',
    'category': '',
    'summary': 'Point of Sale Updates for GBSG',
    'website': 'https://www.icq24.com',
    'author': 'Angstrom Mena',
    'version': '1.0',
    'description': """
Point of Sale Updates for GBSG
=======================
        """,
    'depends': ['point_of_sale','base'],
    'installable': True,
    'data': ['views/point_of_sale.xml',
             'views/res_partner_view.xml'],
    'qweb': ['static/src/xml/pos.xml'],
    'auto_install': True,
}