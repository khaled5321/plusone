# -*- coding: utf-8 -*-
{
    "name": "my_module",
    "summary": """Plusone Task""",
    "author": "Khaled Emad",
    "category": "Service",
    "version": "16.0.0.1",
    "license": "AGPL-3",
    "depends": ["base"],
    "installable": True,
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/lesson_menu.xml",
        "views/subject_menu.xml",
        "data/subjects.xml",
        "data/users.xml",
    ],
}
