# -*- coding: utf-8 -*-
# from odoo import http


# class PrivateLesson(http.Controller):
#     @http.route('/private_lesson/private_lesson', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/private_lesson/private_lesson/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('private_lesson.listing', {
#             'root': '/private_lesson/private_lesson',
#             'objects': http.request.env['private_lesson.private_lesson'].search([]),
#         })

#     @http.route('/private_lesson/private_lesson/objects/<model("private_lesson.private_lesson"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('private_lesson.object', {
#             'object': obj
#         })
