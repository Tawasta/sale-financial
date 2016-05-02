# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jarmo Kortetjärvi
#    Copyright 2015 Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################
{
    'name': 'Sale-Opportunity Integration',
    'category': 'Sale',
    'version': '8.0.0.3.3',
    'author': 'Oy Tawasta Technologies Ltd.',
    'website': 'http://www.tawasta.fi',
    'depends': [
        'crm',
        'crm_lead_to_sale',
        'crm_simplification',
        'sale',
        'sale_crm',
    ],
    'data': [
        'views/crm_lead_form.xml',

        'views/crm_case_stage_form.xml',
        'views/crm_case_stage_tree.xml',

        'data/crm_case_stage_data.xml',
    ],
}