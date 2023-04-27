from odoo import models, fields
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT


class TaxReport(models.AbstractModel):
    _name = "report.account.tax.report"

    start_date = fields.Date(string="Start Date", required=True, default=lambda x: datetime.today().replace(day=1))
    end_date = fields.Date(string="End Date", required=True, default=fields.Date.today())

    def get_tax_amounts(self, start_date, end_date, tax_id):
        invoice_taxed = 0.0
        invoice_untaxed = 0.0
        invoice = 0.0
        tax_colected = 0.0

        invoice_tax_ids = self.env['account.invoice.tax'].search(
            [('invoice_id.date_invoice', '>=', datetime.strptime(start_date, DEFAULT_SERVER_DATE_FORMAT)),
             ('invoice_id.date_invoice', '<=', datetime.strptime(end_date, DEFAULT_SERVER_DATE_FORMAT)),
             ('tax_id', '=', tax_id.id)])

        for invoice_tax_id in invoice_tax_ids:
            invoice_taxed += invoice_tax_id.base
            tax_colected += invoice_tax_id.amount

        return {
            'invoice': invoice,
            'invoice_taxed': invoice_taxed,
            'invoice_untaxed': invoice_untaxed,
            'tax_colected': tax_colected,
        }

    def get_untax_amount(self, start_date, end_date):
        invoiced = 0.0
        invoice_tax_ids = self.env['account.invoice.line'].search(
            [('invoice_id.date_invoice', '>=', datetime.strptime(start_date, DEFAULT_SERVER_DATE_FORMAT)),
             ('invoice_id.date_invoice', '<=', datetime.strptime(end_date, DEFAULT_SERVER_DATE_FORMAT)),
             ('invoice_line_tax_ids', '=', False)])
        for invoice_tax_id in invoice_tax_ids:
            invoiced += invoice_tax_id.price_unit
        return {
            'invoiced': invoiced,
        }