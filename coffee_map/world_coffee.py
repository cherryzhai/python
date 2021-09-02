import json
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
#from pygal_maps_world.i18n import COUNTRIES
from country_codes import get_country_code

filename = 'coffee_production_data.json'
with open(filename) as f:
    pro_data = json.load(f)

coffee_production = {}
for pro_dict in pro_data:
    if pro_dict['Year'] == '2010':
        country_name = pro_dict['Country Name']
        production = int(float(pro_dict['Value']))
        code = get_country_code(country_name)
        if country_name == 'Tanzania':
            code = TZA
        if code:
            coffee_production[code] = production
            #print(code + ":" + str(proulation))
#            else:
#            print('ERROR -' + country_name)
cc_pros_1,cc_pros_2,cc_pros_3 = {},{},{}
for cc, pro in coffee_production.items():
    if pro<10000000:
        cc_pros_1[cc] = pro
    elif pro<1000000000:
        cc_pros_2[cc] = pro
    else:
        cc_pros_3[cc] = pro

print(len(cc_pros_1),len(cc_pros_2),len(cc_pros_3))

wm_style = LightColorizedStyle
#wm_style = RotateStyle('#366393')
#wm = pygal.maps.world.World()
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World Coffee_Production in 2013, by country'
#wm.add('2010',cc_proulation)
wm.add('0-10m',cc_pros_1)
wm.add('10m-1bn',cc_pros_2)
wm.add('>1bn',cc_pros_3)
wm.render_to_file('world_coffee_production.svg')

#for country_code in sorted(COUNTRIES.keys()):
#    print(country_code, COUNTRIES[country_code])


