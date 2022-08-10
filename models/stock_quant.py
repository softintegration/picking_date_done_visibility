# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.model_create_multi
    def create(self, vals):
        if self.env.context.get('manual_date_done',False):
            for vals_el in vals:
                vals_el.update({'in_date':self.env.context['manual_date_done']})
        return super(StockQuant, self).create(vals)