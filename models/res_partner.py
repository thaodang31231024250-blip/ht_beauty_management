# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthday = fields.Date(string='Ngày sinh')
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác')
    ], string='Giới tính')
    medical_history = fields.Text(string='Tiền sử bệnh lý')
    allergy_note = fields.Text(string='Thông tin dị ứng')
    skin_condition = fields.Selection([
        ('acne', 'Mụn'),
        ('dry', 'Da khô'),
        ('oily', 'Da dầu'),
        ('sensitive', 'Da nhạy cảm'),
    ], string='Tình trạng da')
    source_note = fields.Char(string='Nguồn khách')

    @api.constrains('phone', 'mobile')
    def _check_duplicate_phone(self):
        for record in self:
            phones = list(filter(None, [record.phone, record.mobile]))
            if not phones:
                continue

            # Sử dụng tuple domain chặt chẽ để tránh lỗi đa công ty (multi-company) làm lỗi toán tử OR
            domain = [
                ('id', '!=', record.id),
                '|',
                ('phone', 'in', phones),
                ('mobile', 'in', phones)
            ]
            
            duplicate = self.search(domain, limit=1)
            if duplicate:
                raise ValidationError(f"Số điện thoại hoặc số di động ({', '.join(phones)}) đã tồn tại trong hệ thống.")