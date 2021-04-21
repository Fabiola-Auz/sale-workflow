# Copyright 2021 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockMove(models.Model):

    _inherit = "stock.move"

    related_sale_line_id = fields.Many2one(comodel_name="sale.order.line", index=True,)

    def _prepare_procurement_values(self):
        res = super()._prepare_procurement_values()
        if self.sale_line_id or self.related_sale_line_id:
            res.update(
                {
                    "related_sale_line_id": self.related_sale_line_id.id
                    or self.sale_line_id.id
                    or False,
                }
            )
        return res
