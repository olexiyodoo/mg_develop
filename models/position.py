from odoo import fields, models


class MgPosition(models.Model):
    _name = 'mg.position'
    _description = 'Position'

    name = fields.Char(string='Посада')
    job_duties = fields.Text(string='Посадові обовязки')

