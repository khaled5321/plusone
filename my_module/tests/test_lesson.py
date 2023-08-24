from odoo.tests.common import TransactionCase


class TestLesson(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestLesson, self).setUp(*args, **kwargs)

        self.User = self.env["res.partner"]
        self.Lesson = self.env["my_module.private_lesson"]
        self.Subject = self.env["my_module.subject"]

        self.student = self.User.create(
            {
                "name": "Student",
                "country_id": 1,
            }
        )

        self.teacher = self.User.create(
            {
                "name": "Teacher",
                "country_id": 1,
            }
        )

        self.subject = self.Subject.create(
            {
                "name": "Math",
            }
        )

    def test_lesson_create(self):
        self.math_lesson = self.Lesson.create(
            {
                "subject": self.subject.id,
                "students": self.student,
                "teachers": self.teacher,
            }
        )
        self.assertEqual(self.math_lesson.subject.name, self.subject.name)

        self.assertEqual(
            self.math_lesson.name,
            f"{self.subject.name}-{self.math_lesson.create_date.year}-{self.math_lesson.create_date.month}",
        )

    def test_onchange_students(self):
        self.math_lesson = self.Lesson.create(
            {
                "subject": self.subject.id,
                "students": self.student,
                "teachers": self.teacher,
            }
        )
        expected_result = {
            "domain": {
                "teachers": [
                    ("country_id", "in", [1]),
                    ("id", "not in", [self.student.id]),
                ]
            }
        }
        self.assertEqual(self.math_lesson._onchange_students(), expected_result)
