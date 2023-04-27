from odoo import models, fields


class StockProductReport(models.TransientModel):
    _name = 'stock.product.report'

    product_ids = fields.Many2many('product.template', string='Products')

    def check_report(self):
        if not self.product_ids:
            self.product_ids = self.env['product.template'].search([])
        return self.env.ref('gbs_updates_reports.action_report_stock_product_report').report_action(self)
