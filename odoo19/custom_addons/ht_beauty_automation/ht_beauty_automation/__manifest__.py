{
    'name': 'HT Beauty Automation',
    'version': '1.0',
    'category': 'HT Beauty',
    'summary': 'Tự động hóa thông báo, nhắc lịch và tạo task chăm sóc khách hàng (Bản Community)',
    'author': 'Nhóm F',
    'depends': [
        'mail', 
        'ht_beauty_core', 
        'ht_beauty_appointment', 
        'ht_beauty_treatment'
    ],
    'data': [
        'data/automation_cron.xml',
        # Đã xóa dòng 'data/mail_templates.xml' ở đây
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}