# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class StockMove(models.Model):
    _inherit = "stock.move"

    def _account_entry_move(self):
        """ Accounting Valuation Entries """
        self.ensure_one()
        # if self.product_id.type != 'product':
        #     # no stock valuation for consumable products
        #     return False
        if self.restrict_partner_id:
            # if the move isn't owned by the company, we don't make any valuation
            return False