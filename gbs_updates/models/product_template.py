from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    gbs_average = fields.Monetary(string="GBS Average")