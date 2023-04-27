from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    shop_purchase_limit = fields.Float("Shop Minimum Limit", default="0.0")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        shop_purchase_limit = ICPSudo.get_param('shop_purchase_limit') or False
        res.update(
            shop_purchase_limit= float(shop_purchase_limit),
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param("shop_purchase_limit", self.shop_purchase_limit)
