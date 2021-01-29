{
    'name': 'Updates for GBS',
    'category': 'GBS',
    'summary': 'GBS',
    'website': 'https://www.icq24.com',
    'author': 'Angstrom Mena',
    'version': '1.0',
    'description': """
Updates for GBS
=======================
        """,
    'depends': ['base', 'product', 'sale', 'stock','purchase'],
    'installable': True,
    'data': [
        'security/gbs_group.xml',
        'views/product_template_view.xml',
        'views/sale_order_view.xml',
        'views/point_of_sale.xml',
        'views/purchase_order.xml',
    ],
    'qweb': ['static/src/xml/pos.xml'],
    'auto_install': False,
}

