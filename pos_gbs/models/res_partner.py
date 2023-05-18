import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

   # @api.multi
    def _get_preferred(self):
        for partner_id in self:
            products = []
            product_ids = False
            if self.env[partner_id._name].browse(partner_id.id).exists():
                self.env.cr.execute(
                    "(select product_id from account_invoice_line where product_id is not null and partner_id = %s "
                    "group by product_id)"
                    "union"
                    "(select product_id from pos_order po join pos_order_line pol on "
                    "pol.order_id = po.id where product_id is not null and partner_id = %s group by product_id)",
                    (partner_id.id, partner_id.id))
                product_ids = self.env.cr.fetchall()

            if product_ids:
                products += [product_id[0] for product_id in product_ids]
            partner_id.preferred_products += self.env['product.product'].browse(products)

    preferred_products = fields.Many2many('product.product', string="Preferred Products", compute="_get_preferred")
