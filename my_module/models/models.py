from odoo import models, fields, api


class subject(models.Model):
    _name = "my_module.subject"
    _description = "Subject"

    name = fields.Char(string="Name", required=True)


class private_lesson(models.Model):
    _name = "my_module.private_lesson"
    _description = "Private Lesson"

    subject = fields.Many2one("my_module.subject", string="Subject", required=True)
    name = fields.Char(string="Lesson Name", compute="_compute_name")

    students = fields.Many2many(
        "res.partner",
        "lesson_students",
        string="Students",
        required=True,
        ondelete="cascade",
    )
    teachers = fields.Many2many(
        "res.partner",
        "lesson_teachers",
        string="Teachers",
        required=True,
        ondelete="cascade",
    )

    @api.depends("subject")
    def _compute_name(self):
        for lesson in self:
            if lesson.create_date:
                lesson.name = f"{lesson.subject.name}-{lesson.create_date.year}-{lesson.create_date.month}"
            else:
                lesson.name = ""

    @api.onchange("students")
    def _onchange_students(self):
        return {
            "domain": {
                "teachers": [
                    ("country_id", "in", self.students.mapped("country_id").ids),
                    ("id", "not in", self.students.ids),
                ]
            }
        }
