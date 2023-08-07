from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        self.group_mg_develop_user = self.env.ref(
            'mg_develop.group_mg_develop_user')
        self.group_library_admin = self.env.ref(
            'mg_develop.group_mg_develop_admin')
        self.mg_develop_user = self.env['res.users'].create({
            'name': 'Test User',
            'login': 'test_user',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_mg_develop_user.id)],
        })
        self.mg_develop_admin = self.env['res.users'].create({
            'name': 'Test Admin',
            'login': 'test_admin',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_mg_develop_admin.id)],
        })
        self.developer = self.env['mg.developer'].create({
            'name': 'Demo developer',
            'email': 'test@gmail.com',
        })
        self.company_demo = self.env['mg.company'].create({
            'name': 'Demo company',
            'address': 'USA, NASA, room 322',
        })