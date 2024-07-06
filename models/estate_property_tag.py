from odoo import models, fields


class EstateModelType(models.Model):
    _name = "estate.property.tag"
    _description = "estate type model tags"

    name = fields.Char(required=True)
