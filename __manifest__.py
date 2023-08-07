
{
    'name': "mg_develop",

    'summary': """
        Developers management""",

    'author': "Olexiy Pustovgar",
    'website': "https://github.com/olexiyodoo",

    'category': 'Human Resources',
    'license': 'OPL-1',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/position_data.xml',
        'views/management_menus.xml',
        'views/developer_views.xml',
        'views/position_views.xml',
        'views/company_views.xml',
        #'wizard/developer_multi_wizard_viwes.xml',
    ],
}
