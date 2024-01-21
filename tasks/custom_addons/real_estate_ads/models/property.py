from odoo import fields, models


class Property(models.Model):
    _name = 'estate.property'
    _description = 'Property model description'

    name = fields.Char(String="Name", required = "True")
    tag_ids = fields.Many2many('estate.property.tag', string="Property Tag")
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
    offer_ids = fields.One2many('estate.property.offer', 'property_id', String='Offers')
    sales_id = fields.Many2one('res.users', String="Salesman")
    buyer_id = fields.Many2one('res.partner', String="Buyer", domain=[('is_company', '=', True)])



class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'PropertyType model description'

    name = fields.Char(String="Name", required = "True")




class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'PropertyTag model description'

    name = fields.Char(String="Name", required = "True")


