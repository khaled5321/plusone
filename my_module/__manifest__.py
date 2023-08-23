# -*- coding: utf-8 -*-
{
    "name": "my_module",
    "summary": """Plusone Task""",
    "author": "Khaled Emad",
    "category": "service",
    "version": "16.0.0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    "installable": True,
    "application": True,
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/templates.xml",
        "views/lesson_create_action.xml",
        "views/subject_create_action.xml",
        "views/lesson_menu.xml",
        "views/subject_menu.xml",
        "data/subjects.xml",
        "data/users.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
