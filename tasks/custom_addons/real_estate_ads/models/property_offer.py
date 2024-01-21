from odoo import fields, models


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offers'

    price = fields.Float(string="Price")
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')],
                              string="Status")
    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")
    validity = fields.Integer(string='Validity')
    deadline = fields.Date(string='Deadline', compute='compute_deadline', inverse='_inverse_deadline')
    creation_date = fields.Date(string='Create Date')


