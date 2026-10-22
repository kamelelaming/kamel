# Part of DataMount. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    pos_receipt_logo = fields.Image(
        string="POS Receipt Logo",
        max_width=1024,
        max_height=1024,
        help=(
            "Optional logo printed on receipts from this Point of Sale. "
            "Leave empty to use the company logo."
        ),
    )
    has_pos_receipt_logo = fields.Boolean(
        compute="_compute_has_pos_receipt_logo",
        help="Technical field used by the POS to select the correct receipt logo.",
    )

    @api.depends("pos_receipt_logo")
    def _compute_has_pos_receipt_logo(self):
        for config in self:
            config.has_pos_receipt_logo = bool(config.pos_receipt_logo)
