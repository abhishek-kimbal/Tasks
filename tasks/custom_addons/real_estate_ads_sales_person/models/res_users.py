from odoo import models,fields,api

class Users(models.Model):
    _inherit = "res.users"

    property_ads = fields.One2many("estate.property", "sales_id", string="Property")