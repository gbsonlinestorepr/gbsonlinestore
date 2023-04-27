# -*- coding: utf-8 -*-
{
    'name': 'Chart Account GBSG',
    'category': '',
    'summary': 'Chart Account for GBSG',
    'website': 'https://www.icq24.com',
    'author': 'Angstrom Mena',
    'version': '1.0',
    'description': """""",
    'depends': ['account', 'base_iban'],
    'installable': True,
    'data': ['data/l10n_pr_chart_data.xml',
             'data/account.account.template.csv',
             'data/account_chart_template_data.xml',
             'data/account.tax.template.xml',
             'data/account_chart_template_data.yml'],
    'auto_install': False,
}
