# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError     


class GestorTransaccionCompra(models.Model):
    _name = 'gestor.transaccion.compra'
    _description = 'Gestor de Compras'

    purchase_id = fields.Many2one('purchase.order', string='Numero')
    state = fields.Selection(related='purchase_id.state', string='Estado')
    percentage = fields.Float(string='%')
    total = fields.Float(string='Total', compute='_compute_total')

    parent_id = fields.Many2one('gestor.transaccion')


    @api.depends('percentage', 'purchase_id')
    def _compute_total(self):
        for rec in self:
            total_purchase = rec.purchase_id.amount_total
            rec.total = total_purchase * (rec.percentage / 100)

    
    @api.constrains('percentage')
    def _check_percentage(self):
        for rec in self:
            if rec.percentage < 0 or rec.percentage > 100:
                raise ValidationError("El porcentaje debe ser un valor entre 0 y 100")