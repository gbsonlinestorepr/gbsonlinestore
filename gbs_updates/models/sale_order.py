from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    gbs_average = fields.Monetary(related="product_id.gbs_average")