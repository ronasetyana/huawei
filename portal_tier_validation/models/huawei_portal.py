# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class Approval(models.Model):
    _name = 'huawei_portal.approval'
    _inherit = ["huawei_portal.approval", "tier.validation"]
    _state_from = ["draft", "sent"]
    _state_to = ["approve"]
