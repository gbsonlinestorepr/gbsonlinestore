from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT


class StatalTaxReport(models.TransientModel):
    _name = 'report.account.statal.tax'
    _inherit = 'report.account.tax.report'

    tax_ids = fields.Many2many("account.tax", string="Tax")
    type = fields.Selection([('summarice', 'Summariced'), ('detailed', 'Detailed')], string="Type", required=True,
                            default='summarice')

    def get_other_invoices(self):
        invoice_taxed = 0.0
        invoice_untaxed = 0.0
        invoice = 0.0
        tax_colected = 0.0
        invoice_ids = self.env['account.invoice'].search(
            [('date_invoice', '>=', datetime.strptime(self.start_date, DEFAULT_SERVER_DATE_FORMAT)),
             ('date_invoice', '<=', datetime.strptime(self.end_date, DEFAULT_SERVER_DATE_FORMAT)),
             ('state', 'in', ('open', 'paid')), '|',
             ('tax_line_ids.tax_id', 'not in', self.tax_ids.ids), ('tax_line_ids', '=', False)])
        for invoice_id in invoice_ids:
            invoice += invoice_id.amount_total
            tax_colected += invoice_id.amount_tax
            if invoice_id.amount_tax != 0:
                invoice_taxed += invoice_id.amount_untaxed
            else:
                invoice_untaxed += invoice_id.amount_total
        return {
            'invoice': invoice,
            'invoice_taxed': invoice_taxed,
            'invoice_untaxed': invoice_untaxed,
            'tax_colected': tax_colected,
            'display_others': invoice_ids
        }

    def get_amounts(self):
        amounts = []
        if not self.tax_ids:
            self.tax_ids = self.env['account.tax'].search([])

        for tax_id in self.tax_ids:
            amount_values = self.get_tax_amounts(self.start_date, self.end_date, tax_id)
            if amount_values:
                amount_values.update({'tax': tax_id.name})
                amounts.append(amount_values)
        return amounts

    def get_untax_amount(self):
        amounts = super(StatalTaxReport, self).get_untax_amount(self.start_date, self.end_date)
        return amounts

    def get_invoices_summarice(self, tax_id):
        return self.env['account.invoice.tax'].search([('tax_id', '=', tax_id.id),
                                                       ('invoice_id.state', 'in', ('open', 'paid')),
                                                       ('invoice_id.date_invoice', '>=',
                                                        datetime.strptime(self.start_date, DEFAULT_SERVER_DATE_FORMAT)),
                                                       ('invoice_id.date_invoice', '<=',
                                                        datetime.strptime(self.end_date, DEFAULT_SERVER_DATE_FORMAT))])

    def check_report(self):
        if not self.tax_ids:
            self.tax_ids = self.env['account.tax'].search([])

        if self.type == 'summarice':
            return self.env.ref('pr_reports.statal_tax_summarice_report').report_action(self)
        elif self.type == 'detailed':
            return self.env.ref('pr_reports.statal_tax_detailed_report').report_action(self)
