# -*- coding: utf-8 -*--
{
    "name": "Real Estate Ads",
    "version": "1.0",
    "website": "https://theodooguys.com",
    "author": "Abhishek",
    "description": """
    Real estate module to show available properties
    """,
    "category": "Sales",
    "version": '16.0.1.0.0',
    "depends": ["base"],
    "data": [
        #security
        "security/ir.model.access.csv",
        "security/res_groups.xml",
        "security/model_access.xml",
        "security/ir_rule.xml",

        #views
        "views/property_view.xml",
        "views/property_type_view.xml",
        "views/property_tag_view.xml",
        "views/property_offer_view.xml",
        "views/menu_items.xml",

        #Data files
        #"data/property_type.xml",
        "data/estate.property.type.csv",

        # Report
        'report/report_template.xml',
        'report/property_report.xml'
    ],
    "demo":[
        "demo/property_tag.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}