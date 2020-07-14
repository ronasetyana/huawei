# -*- coding: utf-8 -*-
# from odoo import http


# class HuaweiPortal(http.Controller):
#     @http.route('/huawei_portal/huawei_portal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/huawei_portal/huawei_portal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('huawei_portal.listing', {
#             'root': '/huawei_portal/huawei_portal',
#             'objects': http.request.env['huawei_portal.huawei_portal'].search([]),
#         })

#     @http.route('/huawei_portal/huawei_portal/objects/<model("huawei_portal.huawei_portal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('huawei_portal.object', {
#             'object': obj
#         })
