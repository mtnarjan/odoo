# -*- coding: utf-8 -*-
from openerp import http

# class PartnerBusinessId(http.Controller):
#     @http.route('/partner_business_id/partner_business_id/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_business_id/partner_business_id/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_business_id.listing', {
#             'root': '/partner_business_id/partner_business_id',
#             'objects': http.request.env['partner_business_id.partner_business_id'].search([]),
#         })

#     @http.route('/partner_business_id/partner_business_id/objects/<model("partner_business_id.partner_business_id"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_business_id.object', {
#             'object': obj
#         })