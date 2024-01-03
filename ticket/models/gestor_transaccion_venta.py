# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError     

class GestorTransaccionVenta(models.Model):
    _name = 'gestor.transaccion.venta'
    _description = 'Gestor de Ventas'

    sale_id = fields.Many2one('sale.order', string='Numero')
    state = fields.Selection(related='sale_id.state', string='Estado')
    percentage = fields.Float(string='%')
    total = fields.Float(string='Total', compute='_compute_total')

    parent_id = fields.Many2one('gestor.transaccion')

    @api.depends('percentage', 'sale_id')
    def _compute_total(self):
        for rec in self:
            total_sale = rec.sale_id.amount_total
            rec.total = total_sale * (rec.percentage / 100)

    @api.constrains('percentage')
    def _check_percentage(self):
        for rec in self:
            if rec.percentage < 0 or rec.percentage > 100:
                raise ValidationError("El porcentaje debe ser un valor entre 0 y 100")