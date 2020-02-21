# -*- coding: utf-8 -*-
{
    'name': 'Puerto Rico Reports',
    'category': '',
    'summary': 'Puerto Rico Reports',
    'website': 'https://www.icq24.com',
    'author': 'Angstrom Mena',
    'version': '1.0',
    'description': """
Puerto Rico Reports
=======================
        """,
    'depends': ['base', 'account'],
    'installable': True,
    'data': [
        "wizards/municipal_tax_view.xml",
        "reports/municipal_tax_report.xml",
        "wizards/statal_tax_view.xml",
        "reports/statal_tax_report.xml",
        "views/tax_report_view.xml",
        "views/account_invoice_tax_view.xml",
        "views/account_trial_balance_view.xml",
    ],
    'auto_install': False,
}
