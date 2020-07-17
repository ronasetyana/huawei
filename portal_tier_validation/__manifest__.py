# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "portal Tier Validation",
    "summary": "Extends the functionality of portal Orders to "
    "support a tier validation process.",
    "version": "13.0.1.0.0",
    "category": "portals",
    "website": "https://github.com/OCA/portal-workflow",
    "author": "Eficent, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["huawei_portal", "base_tier_validation"],
    "data": ["views/portal_view.xml"],
}
