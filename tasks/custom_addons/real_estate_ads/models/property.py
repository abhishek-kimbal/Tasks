from odoo import fields, models, api


class Property(models.Model):
    _name = 'estate.property'
    _description = 'Property model description'

    name = fields.Char(String="Name", required = "True")

    state = fields.Selection([("new","New"),
                              ("received", "Offer Received"),
                              ("accepted","Offer Accepted"),
                              ("sold","Sold"),
                              ("cancel","cancelled")],
                              default="new", string="Status")

    tag_ids = fields.Many2many('estate.property.tag', string="Property Tag")
    type_id = fields.Many2one('estate.property.type', string="Property Type")
    description = fields.Text(String="Description")
    postcode = fields.Char(String="postcode")
    data_availability = fields.Date(String="Available From")
    expected_price = fields.Float(String="Expected Price")
    best_offer = fields.Float(String="Best Offer", compute="_compute_best_price")
    selling_price = fields.Float(String="Selling Price", readonly=True)
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
    phone = fields.Char(String="Phone", related= "buyer_id.phone")

    @api.onchange('living_area', 'garden_area')
    def _onchange_total_area(self):
        self.total_area = self.living_area + self.garden_area

    total_area = fields.Integer(String="Total Area")

    def action_sold(self):
        self.state = "sold"

    def action_cancel(self):
        self.state = "cancel"


    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)

    offer_count = fields.Integer(String="Offer Count", compute=_compute_offer_count)

    def action_property_view_offers(self):
        return {
            'type': "ir.actions.act_window",
            'name': f"{self.name}  - offers",
            'domain': [('property_id', '=', self.id)],
            'view_mode': 'tree',
            'res_model': 'estate.property.offer'
        }

    @api.depends('offer_ids')
    def _compute_best_price(self):
        for rec in self:
            if rec.offer_ids:
                rec.best_offer = max(rec.offer_ids.mapped('price'))
            else:
                rec.best_offer = 0


    # @api.depends('garden_area', 'living_area')
    # def _compute_total_area(self):
    #     for rec in self:
    #         rec.total_area = rec. garden_area + rec. living_area


    # total_area = fields.Integer(String="Total Area", compute=_compute_total_area)



class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'PropertyType model description'

    name = fields.Char(String="Name", required = "True")




class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'PropertyTag model description'

    name = fields.Char(String="Name", required = "True")
    color = fields.Integer(string="Color")


