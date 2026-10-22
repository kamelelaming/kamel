# POS Receipt Logo by Configuration (Odoo 19)

This module lets each Point of Sale use its own logo on POS receipts.

## Use

1. Install **POS Receipt Logo by Configuration**.
2. Go to **Point of Sale → Configuration → Point of Sales** and open a POS.
3. On the **Configuration** tab, upload **Receipt Logo**.
4. Reload the POS session after changing the logo.

Only that POS uses its configured logo in the POS receipt preview, printing, and
browser-generated PDF. When the field is empty, Odoo keeps using the company
logo. Invoice PDFs are intentionally unchanged.
