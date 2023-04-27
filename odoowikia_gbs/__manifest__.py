# -*- coding: utf-8 -*-
{
    'name': 'Odoowikia GBSG',
    'category': '',
    'summary': '',
    'website': 'https://www.odoowikia.com',
    'author': 'Divya Vyas',
    'version': '1.0',
    'description': """GBSG customization""",
    'depends': [ 'base', 'stock','sale','purchase'],
    'installable': True,
    'data': [
             'data/report_paperformat.xml',
			 'report/delivery_label.xml',
			'views/assets.xml',
              'views/res_config_settings_view.xml',
            'views/template.xml',
             'views/report.xml',

            ],
    'auto_install': True,
}
