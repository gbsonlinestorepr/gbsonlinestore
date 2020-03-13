# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request
from odoo.tools import ustr
from odoo.tools.pycompat import izip

class WebsiteSale(WebsiteSale):

    def get_attribute_value_ids(self, product):
        print ("--------------------", product)
        res = super(WebsiteSale, self).get_attribute_value_ids(product)
        variant_ids = [r[0] for r in res]
        for r, variant in izip(res, request.env['product.product'].sudo().browse(variant_ids)):
             print ("KKKKKKKKKKKKKK", r)
             for i in r:
                 print ("OOOOOOOOOOOOOOOOOO",i)
                 if type(i) == dict :
                     print ("****************")
                     i.update({'virtual_available': variant.qty_available})
        return res

