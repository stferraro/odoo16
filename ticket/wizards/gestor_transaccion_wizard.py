from odoo import models, fields, api
from odoo.exceptions import UserError
import pandas as pd

class GestorTransaccionWizard(models.TransientModel):
    _name = 'gestor.transaccion.wizard'
    _description = 'ventana emergente(wizard)'
 
    state = fields.Selection(
        selection=[('draft', 'Borrador'), ('done', 'Publicado')],
        default='draft',
        string='Estado',
    )
    
    def get_from_db(self):
        query = '''
            SELECT 
                gt.reference, 
                gt.name, 
                c.name as currency_name, 
                co.name as company_name, 
                gt.date 
            FROM 
                gestor_transaccion gt
            LEFT JOIN 
                res_currency c ON gt.currency_id = c.id
            LEFT JOIN 
                res_company co ON gt.company_id = co.id
            WHERE 
                gt.state = %s
            '''
        self._cr.execute(query, (self.state,))
        report = self._cr.dictfetchall()
        values = []
        for record in report:
            values.append({
                'reference': record['reference'],
                'name': record['name'],
                'currency_id': record['currency_name'],
                'company_id': record['company_name'],
                'date': record['date'].strftime('%d/%m/%Y'),
            })
        return {
            'data' : values
        }
    

    def print_report(self):
        data = self.get_from_db()
        return self.env.ref('ticket.action_report_gestor_transaccion').report_action(self, data= data)