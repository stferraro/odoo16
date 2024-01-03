# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class GestorTransaccion(models.Model):
    _name = 'gestor.transaccion'
    _description = 'Gestor de Transacciones'

    name = fields.Char(string='Nombre')
    reference = fields.Char(string='Ticket', readonly=True, default=lambda self: _('New'))
    date = fields.Date(string='Fecha')
    currency_id = fields.Many2one('res.currency', string='Moneda') 
    company_id = fields.Many2one('res.company', string="Compañia")

    state = fields.Selection(
        selection=[('draft', 'Borrador'), ('done', 'Publicado')],
        default='draft',
        string='Estado',
    )

    sale_ids = fields.One2many('gestor.transaccion.venta','parent_id',string='Ventas')
    purchase_ids = fields.One2many('gestor.transaccion.compra','parent_id',string='Ventas')

    def action_confirm(self):
        self.state = 'done'

    @api.model
    def create(self, vals):
        if vals.get('reference',_('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('ticket.gestor.transaccion') or _('New')
        res = super(GestorTransaccion, self).create(vals)
        return res

    
        

    
    
    