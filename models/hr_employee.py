# -*- coding: utf-8 -*-
from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    role_type = fields.Selection([
        ('doctor', 'Bác sĩ'),
        ('ktv', 'Kỹ thuật viên'),
        ('receptionist', 'Lễ tân'),
        ('cskh', 'CSKH'),
    ], string='Vai trò', required=True, tracking=True)

    specialization = fields.Selection([
        ('skin', 'Da liễu'),
        ('acne', 'Trị mụn'),
        ('laser', 'Laser'),
        ('anti_aging', 'Trẻ hóa'),
    ], string='Chuyên môn')