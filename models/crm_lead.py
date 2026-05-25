# -*- coding: utf-8 -*-
from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    zalo_link = fields.Char(string='Zalo Link', tracking=True)