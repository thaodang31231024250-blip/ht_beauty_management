from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Liên kết 1 khách hàng -> Nhiều phác đồ
    treatment_plan_ids = fields.One2many('beauty.treatment.plan', 'partner_id', string='Danh sách phác đồ')
    
    # Biến đếm số lượng phác đồ để hiển thị lên nút bấm
    treatment_plan_count = fields.Integer(string='Số lượng phác đồ', compute='_compute_treatment_plan_count')

    def _compute_treatment_plan_count(self):
        for partner in self:
            partner.treatment_plan_count = len(partner.treatment_plan_ids)

    # Hàm khi click vào nút bấm sẽ mở ra danh sách các phác đồ CỦA RIÊNG KHÁCH ĐÓ
    def action_view_treatment_plans(self):
        self.ensure_one()
        return {
            'name': 'Phác đồ điều trị của %s' % self.name,
            'type': 'ir.actions.act_window',
            'res_model': 'beauty.treatment.plan',
            'view_mode': 'list,form',
            'domain': [('partner_id', '=', self.id)], # Chỉ lọc phác đồ của người này
            'context': {'default_partner_id': self.id}, # Khi ấn "Tạo mới", tự động điền tên người này
        }