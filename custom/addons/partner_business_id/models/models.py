# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions

_INVALID_MSG = "The Business ID (Y-tunnus) [{:s}] seems to be incorrect."

class partner_business_id(models.Model):
    
    _inherit = 'res.partner'
    
    business_id = fields.Char(string="Y-tunnus")
    
    @api.one
    @api.constrains('business_id')
    def _check_business_id(self):
        # Allow for Null values:
        if self.business_id == False:
            return
        try:
            if not self._check_id(self.business_id):
                raise exceptions.ValidationError(_INVALID_MSG.format(str(self.business_id)))
        except Exception:
            raise exceptions.ValidationError(_INVALID_MSG.format(str(self.business_id)))
        
    @api.onchange('vat')
    def _onchange_vat(self):
        if str(self.vat).startswith("FI"):
            self.business_id = self.vat[2:-1] + "-" + self.vat[-1]
    
    def _check_id(self, business_id):
        '''
        Validate business_id.
        http://tarkistusmerkit.teppovuori.fi/tarkmerk.htm#y-tunnus2
        '''
        if len(business_id) == 8:
            business_id = "0" + business_id
        if len(business_id) != 9:
            return False
        for c in business_id:
            if c not in "0123456789-":
                return False
        split_id = business_id.split('-')
        base = split_id[0]
        check = split_id[1]
        factors = [7, 9, 10, 5, 8, 4, 2]
        if len(base) != 7 or len(check) != 1:
            return False
        check = int(check)
        product_sum = 0
        for i in range(7):
            product_sum += int(base[i]) * factors[i]
        remainder = product_sum % 11
        if remainder == 0 and check == 0:
            return True
        if remainder == 1:
            return False
        return 11 - remainder == check
    
# class partner_business_id(models.Model):
#     _name = 'partner_business_id.partner_business_id'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100