# -*- coding: utf-8 -*-
from odoo import models, fields

class BeautyRoom(models.Model):
    _name = 'beauty.room'
    _description = 'Beauty Treatment Room'
    _rec_name = 'name'
    _order = 'name asc'

    name = fields.Char(string='Tên phòng', required=True, tracking=True)
    code = fields.Char(string='Mã phòng', required=True, tracking=True)
    area = fields.Float(string='Diện tích')
    capacity = fields.Integer(string='Sức chứa')
    room_type = fields.Selection([
        ('treatment', 'Phòng điều trị'),
        ('laser', 'Phòng laser'),
        ('consulting', 'Phòng tư vấn'),
    ], string='Loại phòng')
    status = fields.Selection([
        ('free', 'Trống'),
        ('in_use', 'Đang sử dụng'),
        ('maintenance', 'Bảo trì'),
    ], string='Trạng thái', default='free', required=True, tracking=True)
    note = fields.Text(string='Ghi chú')
    active = fields.Boolean(default=True)