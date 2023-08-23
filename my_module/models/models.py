from odoo import models, fields, api


class subject(models.Model):
    _name = "my_module.subject"

    name = fields.Char(string="Name", required=True)


class private_lesson(models.Model):
    _name = "my_module.private_lesson"

    subject = fields.Many2one("my_module.subject", string="Subject")
    lesson_name = fields.Char(string="Lesson Name", compute="_compute_lesson_name")

    student_id = fields.Many2one("res.partner", string="Student", required=True)
    teacher_id = fields.Many2one("res.partner", string="Teacher", required=True)

    @api.depends("subject", "create_date")
    def _compute_lesson_name(self):
        for lesson in self:
            lesson.lesson_name = (
                f"{lesson.subject}-{lesson.create_date.year}-{lesson.create_date.month}"
            )

    @api.onchange("student_id")
    def _onchange_student_id(self):
        self.teacher_id = False
        if self.student_id:
            country_id = self.student_id.country_id
            self.teacher_id = self.env["res.partner"].search(
                [("country_id", "=", country_id)]
            )