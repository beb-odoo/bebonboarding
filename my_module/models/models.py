# -*- coding: utf-8 -*-

from unidecode import unidecode
from odoo import models, fields, api

class my_module(models.Model):
     _name = 'my_module.my_module'
     _description = 'test'
     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
     start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
     @api.model
     def create(self, values):
         if 'name' in values:
             values['name'] = unidecode(values['name'])
         return super(my_module, self).create(values)

     @api.multi
     def write(self, values):
         if 'name' in values:
             values['name'] = unidecode(values['name'])
         return super(my_module, self).write(values)
     @api.depends('value')
     def _value_pc(self):
         self.value2 = float(self.value) / 100
