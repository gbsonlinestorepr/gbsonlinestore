# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request
from odoo.tools import ustr
import logging
_logger = logging.getLogger(__name__)
from odoo.tools.pycompat import izip

class WebsiteSale(WebsiteSale):

    def get_attribute_value_ids(self, product):
        res = super(WebsiteSale, self).get_attribute_value_ids(product)
        variant_ids = [r[0] for r in res]
        for r, variant in izip(res, request.env['product.product'].sudo().browse(variant_ids)):
            r.extend([{
                'virtual_available': variant.qty_available,
                'product_type': variant.type,
                'inventory_availability': variant.inventory_availability,
                'available_threshold': variant.available_threshold,
                'custom_message': variant.custom_message,
                'product_template': variant.product_tmpl_id.id,
                'cart_qty': variant.cart_qty,
                'uom_name': variant.uom_id.name,
            }])
        '''print ("KKKKKKKKKKKKKK", r)
            for i in r:
                _logger.info("----------------------." + str(i))
                if type(i) == dict :
                    print ("****************")
                    i.update({'virtual_available': variant.qty_available})'''
        return res

