# -*- coding: utf-8 -*-
{
    'name': "Ticket",
    'summary': "Gestor de Ventas y Compras",
    'description': "pequeña aplicación en odoo",
    'author': "CorpoEureka",
    'website': "https://www.yourcompany.com",
    'sequence' : -100,
    'version': '0.1',
    'license': 'LGPL-3',
    'depends': ['sale', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/vista_gestor_transaccion.xml',
        'wizards/gestor_transaccion_wizard.xml',
        'views/menuitems.xml',
        'reports/sale_card.xml',
        'reports/purchase_card.xml',
        'reports/report_detail.xml',
        'reports/report.xml'
    ],
    'application':True,
    'installable':True,
    'auto_install':False,
     'images': ['static/description/icon.png'],
}
