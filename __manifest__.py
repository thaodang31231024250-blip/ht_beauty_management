# -*- coding: utf-8 -*-
{
    'name': 'HT Beauty Core',
    'version': '1.0',
    'summary': 'Core module for HT Beauty Clinic Management',
    'author': 'HT Beauty',
    'category': 'Services',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'crm',
        'hr',
        'sale_management',
        'website',
        'website_crm',
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/hr_employee_views.xml',
        'views/res_partner_views.xml',
        'views/beauty_room_views.xml',
        'views/menu.xml',  # Bắt buộc nằm ở cuối cùng sau các file view
    ],
    'installable': True,
    'application': True,
}