from odoo import _, fields, models


class DeveloperMultiWizard(models.TransientModel):
    _name = 'mg.developer.multi.wizard'
    _description = 'Wizard to create link developer to company'

    developer_id = fields.Many2one('mg.developer', 'Developer')
    company_id = fields.Many2one('mg.developer', 'Company'))

    def action_open_wizard(self):
        return {
            'name': _('Linked Wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mg.developer.multi.wizard',
            'target': 'new',

        }
