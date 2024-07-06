from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate property"

    name = fields.Char(required=True)
    description = (
        fields.Text(default="when duplicated,status and date are not copied"))
    post_code = fields.Char()
    date_availability = (
        fields.Date(defult=fields.Date.add(fields.Date.today(), months=3)))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('North', 'North'), ('south', 'south'), ('west', 'west'),
                   ('east', 'east')])
    status = fields.Selection(default='New', copy=False,
                              selection=[('New', 'New'),
                                         ('Offer Received', 'Offer Received'),
                                         ('Offer Accepted', 'Offer Accepted'),
                                         ('Sold', 'Sold'),
                                         ('Canceled', 'Canceled')])
    active = fields.Boolean('Active', default=True)
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    property_type = fields.Many2one("estate.property.type")
    buyer = fields.Many2one('res.partner', string='buyer')
    salesman = fields.Many2one('res.users', string='salesman')
    property_tag = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer',
                                inverse_name='property_id')
