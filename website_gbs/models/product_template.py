from odoo import models, fields
import math


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def get_rating(self):
        mail_message_ids = self.env['mail.message'].search_read([('res_id', '=', self.id),
                                                                 ('model', '=', 'product.template'),
                                                                 ('subtype_id', '=', 1),
                                                                 ('rating_value', '>', 0)], ['rating_value'])
        rating_amount = sum(int(x.get('rating_value')) for x in mail_message_ids) / (len(mail_message_ids) or 1)

        val_integer = math.floor(rating_amount)
        val_decimal = rating_amount - val_integer
        empty_star = 5 - (val_integer + math.ceil(val_decimal))

        return {'val_integer': val_integer,
                'val_decimal': val_decimal,
                'empty_star': empty_star}

    description_short = fields.Text(string="Short Description")