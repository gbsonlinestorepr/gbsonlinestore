from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    exempt_taxes = fields.Many2many('account.tax', string="Exempts Taxes")