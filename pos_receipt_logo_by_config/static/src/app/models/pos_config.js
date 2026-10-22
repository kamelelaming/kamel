/** @odoo-module **/

import { PosConfig } from "@point_of_sale/app/models/pos_config";
import { imageUrl } from "@web/core/utils/urls";
import { patch } from "@web/core/utils/patch";

patch(PosConfig.prototype, {
    get receiptCompanyLogoUrl() {
        if (this.has_pos_receipt_logo) {
            return imageUrl("pos.config", this.id, "pos_receipt_logo", {
                width: 256,
                height: 256,
            });
        }
        return super.receiptCompanyLogoUrl;
    },
});
