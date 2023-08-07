from odoo.addons.mg_develop.tests.common import TestCommon
from odoo.tests import tagged
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install', 'mg_develop', 'access')
class TestAccessRights(TestCommon):

    def test_01_mg_develop_user_access_rights(self):
        with self.assertRaises(AccessError):
            self.env['mg.company'].with_user(self.mg_develop_user).create(
                {'name': 'Test company'})
        with self.assertRaises(AccessError):
            self.company_demo.with_user(self.mg_develop_user).unlink()

    def test_02_mg_develop_admin_access_rights(self):
        company = self.env['mg.company'].with_user(self.mg_develop_admin).create(
            {'name': 'Test Company'})
        company.with_user(self.mg_develop_admin).read()
        company.with_user(self.mg_develop_admin).write({'name': 'Test Company Next'})
        company.with_user(self.mg_develop_admin).unlink()