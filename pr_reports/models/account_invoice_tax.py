from odoo import models, fields


class AccountInvoiceTax(models.Model):
    _inherit = 'account.tax'
   # _inherit = 'account.invoice.tax'

    invoice_state = fields.Selection(related="invoice_id.state")
    invoice_partner_id = fields.Many2one(related='invoice_id.partner_id')
    invoice_date = fields.Date(related='invoice_id.date_invoice', store=True)

    amount_total = fields.Monetary(string="Tax")
    amount = fields.Monetary(string="Tax")
    base = fields.Monetary(string="Taxable Amount")
