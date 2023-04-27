from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT


class MunicipalTaxReport(models.TransientModel):
    _name = 'report.account.municipal.tax'
    _inherit = 'report.account.tax.report'

    tax_id = fields.Many2one("account.tax", string="Tax", required=True)

    def get_amount(self):
        return self.get_tax_amounts(self.start_date, self.end_date, self.tax_id)

    def check_report(self):
        return self.env.ref('pr_reports.municipal_tax_report').report_action(self)
