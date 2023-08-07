from odoo import fields, models


class MgDeveloper(models.Model):
    _name = 'mg.developer'
    _description = 'Developers'

    name = fields.Char(string='ПІБ')
    phone = fields.Char(string='Телефон')
    email = fields.Char(string='E-mail')
    address = fields.Text(string='Адреса')
    birth_date = fields.Date(string='Дата народження')
    position_id = fields.Many2one(
        comodel_name='mg.position',
        string='Посада',
    )
    company_id = fields.Many2one(
        comodel_name='mg.company',
        string='Компанія',
    )

