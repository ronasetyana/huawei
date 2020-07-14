# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HuaweiPortal(models.Model):
    _name = 'huawei_portal.huawei_portal'
    _description = 'SLA'

    date = fields.Datetime(string='Date', required=True)
    sla_category = fields.Many2one(related='sla_id.category', string='Category', store=True)
    sla_id = fields.Many2one('huawei_portal.sla', string='SLA', store=True)
    baseline = fields.Float(string='Baseline', store=True, group_operator='avg')
    target = fields.Float(related='sla_id.target', string='Target', store=True, group_operator='avg')
    area = fields.Many2one('huawei_portal.area', string='Area', store=True)
    actual = fields.Float(string='Actual', store=True, group_operator='avg')
    sla_weight = fields.Float(related='sla_id.weight', string='SLA Weight', store=True, group_operator='avg')
    sc_allocated = fields.Float(string='SC Allocated', store=True, group_operator='avg')
    sla_allowable_gap = fields.Float(related='sla_id.allowable_gap', string='Allowable Gap', store=True, group_operator='avg')
    performance_gap = fields.Float(compute='_compute_performance_gap', string='Performance Gap', store=True, group_operator='avg')
    sc_due = fields.Datetime(string='SC Due', store=True)
    sc_offset = fields.Float(string='SC Offset', store=True, group_operator='avg')

    @api.depends('target', 'actual')
    def _compute_performance_gap(self):
        self.performance_gap = self.actual - self.target

    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100


class Brand(models.Model):
    _name = 'huawei_portal.brand'
    name = fields.Char(string='Brand')


class Area(models.Model):
    _name = 'huawei_portal.area'
    name = fields.Char(string='Area')


class SLACategory(models.Model):
    _name = 'huawei_portal.sla_category'
    name = fields.Char(string='Category')


class SLA(models.Model):
    _name = 'huawei_portal.sla'
    category = fields.Many2one('huawei_portal.sla_category', string='Category')
    name = fields.Char(string='SLA')
    target = fields.Float(string='Target')
    weight = fields.Float(string='Weight')
    allowable_gap = fields.Float(string='Allowable Gap')


