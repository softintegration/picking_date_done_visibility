# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _action_done(self):
        """ Inherit picking _action_done to allow user with proper access rights to edit the date_done
        manually"""
        manual_date_done = self.date_done
        # we have to add the manual_date_done in the context to detect this date in the case of the first
        # incoming of product that will create new stock.quant,in this case we have to set the in_date
        # of stock.quant as manual_date_done
        res = super(StockPicking, self.with_context(manual_date_done=manual_date_done))._action_done()
        if not manual_date_done:
            return res
        self.write({'date_done':manual_date_done})
        self._apply_date_done(manual_date_done)
        return res

    def _apply_date_done(self,manual_date_done):
        """ Update the date of the related move_lines and move_line_ids with the given manual_date_done"""
        move_lines = self.mapped("move_lines")
        move_line_ids = self.mapped("move_line_ids")
        move_lines.write({'date':manual_date_done})
        move_line_ids.write({'date':manual_date_done})
        return True
