from odoo import models, fields


class EstateModelType(models.Model):
    _name = "estate.property.type"
    _description = "estate type model"

    name = fields.Char()

