# -*- coding: utf-8 -*-
{
    "name": "private_lesson",
    "summary": """Plusone Task""",
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "private_lesson",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    "installable": True,
    "application": True,
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/templates.xml",
        "views/menu.xml",
        # "data/subjects.csv",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
