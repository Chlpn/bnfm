# -*- coding: utf-8 -*-

from odoo import fields, models

class QuotationSubject(models.Model):
    _inherit ="sale.order"

    subject = fields.Char(string="Subject")