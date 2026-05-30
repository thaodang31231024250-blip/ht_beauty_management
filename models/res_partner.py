# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartnerTreatment(models.Model):
    _inherit = 'res.partner'

    treatment_plan_ids = fields.One2many('beauty.treatment.plan', 'partner_id', string='Phác đồ điều trị')
    treatment_plan_count = fields.Integer(string='Số phác đồ', compute='_compute_treatment_plan_count')

    @api.depends('treatment_plan_ids')
    def _compute_treatment_plan_count(self):
        for record in self:
            record.treatment_plan_count = len(record.treatment_plan_ids)

    def action_view_treatment_plans(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Phác đồ điều trị',
            'res_model': 'beauty.treatment.plan',
            'view_mode': 'list,form',
            'domain': [('partner_id', '=', self.id)],
            'context': {'default_partner_id': self.id},
        }
