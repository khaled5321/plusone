from odoo import models, fields, api


class subject(models.Model):
    _name = "my_module.subject"
    _description = "Subject"

    name = fields.Char(string="Name", required=True)


class private_lesson(models.Model):
    _name = "my_module.private_lesson"
    _description = "Private Lesson"

    subject = fields.Many2one("my_module.subject", string="Subject", required=True)
    lesson_name = fields.Char(string="Lesson Name", compute="_compute_lesson_name")

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
        # domain="[('country_id', 'in', students.country_id)]"
    )

    @api.depends("subject")
    def _compute_lesson_name(self):
        for lesson in self:
            if lesson.create_date:
                lesson.lesson_name = f"{lesson.subject.name}-{lesson.create_date.year}-{lesson.create_date.month}"
            else:
                lesson.lesson_name = ""
