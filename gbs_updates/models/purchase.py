from odoo import models, fields
from datetime import datetime
from datetime import timedelta


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    date_confirm = fields.Datetime('Date Confirm')

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        self.date_confirm = datetime.now()
        # date_confirm_new=datetime.now() - timedelta(hours=4)
        # now_utc = datetime.now(timezone('UTC -4'))
        # print(now_utc.strftime(fmt))
        # self.date_confirm = datetime.today().replace(day=1)
        return res
