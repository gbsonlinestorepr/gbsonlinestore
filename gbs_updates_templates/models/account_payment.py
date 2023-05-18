from odoo import models, api


class AccountPayment(models.Model):
    _inherit = 'account.payment'

   # @api.multi
    def do_print_checks(self):
        return self.env.ref('gbs_updates_templates.action_report_payment_receipt_gbs').report_action(self)
