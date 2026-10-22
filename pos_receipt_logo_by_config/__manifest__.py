# Part of DataMount. See LICENSE file for full copyright and licensing details.

{
    "name": "POS Receipt Logo by Configuration",
    "version": "19.0.1.0.0",
    "category": "Sales/Point of Sale",
    "summary": "Use an optional, POS-specific logo on POS receipts.",
    "description": """
POS Receipt Logo by Configuration
=================================
Add an optional receipt logo to each Point of Sale configuration.

When a logo is configured, only POS receipts from that Point of Sale use it.
Point of Sales without a configured logo continue to use the company logo.
""",
    "author": "DataMount",
    "depends": ["point_of_sale"],
    "data": [
        "views/pos_config_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_receipt_logo_by_config/static/src/app/models/pos_config.js",
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
