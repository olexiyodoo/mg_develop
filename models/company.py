from odoo import fields, models


class MgCompany(models.Model):
    _name = 'mg.company'
    _description = 'Companies'

    name = fields.Char(string='Назва компанії')
    address = fields.Text(string='Юридична адреса')
    developer_ids = fields.One2many(
        comodel_name='mg.developer',
        inverse_name='company_id',
        string='Розробники',
    )
