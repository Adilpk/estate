{
    'name' : 'estates',
    'version' : '1.0',
    'sequence' : 2,
    'category' : 'estate/estate',
    'depends': ['base','web'],
    'description': """ this is estate module """,
    'application': True,
    'data' : ['security/ir.model.access.csv',
              'views/estate_property_views.xml',
              'views/estate_type_views.xml',
              'views/estate_tag.xml',
              'views/estate_property_offer.xml',
              'views/estate_menus.xml',
              ],
    'demo': [
              'demo/demo_data.xml',
            ],
}