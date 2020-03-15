# -*- coding: utf-8 -*-
{
    'name': 'Odoowikia GBSG',
    'category': '',
    'summary': '',
    'website': 'https://www.odoowikia.com',
    'author': 'Divya Vyas',
    'version': '1.0',
    'description': """GBSG customization""",
    'depends': [ 'base', 'stock','sale'],
    'installable': True,
    'data': [
             'data/report_paperformat.xml',
			 'report/delivery_label.xml',
             'views/report.xml',

            ],
    'auto_install': True,
}
