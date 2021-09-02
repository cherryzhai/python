import csv
import json
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
#from pygal_maps_world.i18n import COUNTRIES
from country_codes import get_country_code

pro_dic = {}

filename = 'coffee_production.csv'
with open(filename) as f:
    reader_csv = csv.reader(f)
#    row = next(reader_csv)
    
    for read_row in reader_csv:
        try:
            country_name = read_row[0]
            production = int(read_row[1])
        except IndexError:
            print('end data')
        else:
            print(country_name)
            code = get_country_code(country_name)
            if code:
                print(code)
                pro_dic[code] = production
                #pro_dic['Value']=production
    
    print(pro_dic)

#filename_store = 'coffee_production_data.json'

cc_pros_1,cc_pros_2,cc_pros_3 = {},{},{}
for cc, pro in pro_dic.items():
    if pro<1000000:
        cc_pros_1[cc] = pro
    elif pro<5000000:
        cc_pros_2[cc] = pro
    else:
        cc_pros_3[cc] = pro

print(len(cc_pros_1),len(cc_pros_2),len(cc_pros_3))

wm_style = LightColorizedStyle
#wm_style = RotateStyle('#366393')
#wm = pygal.maps.world.World()
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World Coffee_Production in 2013, by country'
#wm.add('Africa')
#wm.add('Burundi,167000 Ethiopia,6600000 Kenya,850000 Malawi,30000 Rwanda,300000\tTanzania,750000\tZambia,10000',cc_pros_1)
wm.add('0-1m',cc_pros_1)
wm.add('1m-5m',cc_pros_2)
wm.add('>5m',cc_pros_3)
wm.render_to_file('world_coffee_production.svg')

#for country_code in sorted(COUNTRIES.keys()):
#    print(country_code, COUNTRIES[country_code])

