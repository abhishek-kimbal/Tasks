from odoo import fields, models


class Property(models.Model):
    _name = 'estate.property'
    _description = 'Property model description'

    name = fields.Char(String="Name", required = "True")
    type_id = fields.Many2one('estate.property.type', string="Property Type")
    description = fields.Text(String="Description")
    postcode = fields.Char(String="postcode")
    data_availability = fields.Date(String="Available From")
    expected_price = fields.Float(String="Expected Price")
    best_offer = fields.Float(String="Best Offer")
    selling_price = fields.Float(String="Selling Price")
    bedrooms = fields.Integer(String="Bedrooms")
    living_area = fields.Integer(String="Living Area(sqm)")
    facades = fields.Integer(String="Facades")
    garage = fields.Boolean(String="Garage", default=False)
    garden = fields.Boolean(String="Garden", default=False)
    garden_area = fields.Integer(String="Garden Area")
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
                                          String="Garden Orientation", default='north')



class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'model description'

    name = fields.Char(String="Name", required = "True")


