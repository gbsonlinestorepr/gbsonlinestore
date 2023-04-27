from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    gbs_average = fields.Float(related="product_id.gbs_average")