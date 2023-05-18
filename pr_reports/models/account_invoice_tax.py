from odoo import models, fields


class AccountInvoiceTax(models.Model):
    _inherit = 'account.tax'
   # _inherit = 'account.invoice.tax'

   # invoice_state = fields.Selection(related="account.move.state")
   # invoice_partner_id = fields.Many2one(related='account.move.partner_id')
   # invoice_date = fields.Date(related='account.move.invoice_date', store=True)

    amount_total = fields.Float(string="Tax")
   # amount = fields.Monetary(string="Tax")
    base = fields.Float(string="Taxable Amount")
