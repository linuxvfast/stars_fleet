# -*- coding:utf-8 -*-
from pygal_maps_world.i18n import COUNTRIES

#获取国别码
for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])