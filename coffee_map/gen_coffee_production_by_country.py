import csv
import json
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
#from pygal_maps_world.i18n import COUNTRIES
from country_codes import get_country_code

wm_style = LightColorizedStyle
#wm = pygal.maps.world.World(style = wm_style)
wm = pygal.maps.world.World()
wm.title = 'World Coffee_Production in 2013, by country \n unit:1k bag (60kg/bag)'
#wm.title = 'World Coffee_Production in 2013, by country'

pro_dic = {}

filename = 'coffee_production.csv'
with open(filename) as f:
    reader_csv = csv.reader(f)
#    row = next(reader_csv)
    
    for read_row in reader_csv:
        try:
            country_name = read_row[0]
            production = int(read_row[1])/1000
        except IndexError:
            print('end data')
        else:
            print(country_name)
            code = get_country_code(country_name)
            if code:
                print(code)
                pro_dic[code] = production
                #wm.add(country_name+':'+str(production),code)
                wm.add(country_name,{code:production})
    print(pro_dic)

#wm.add('world coffee',cc_pros)

wm.render_to_file('world_coffee_production_by_country.svg')

#for country_code in sorted(COUNTRIES.keys()):
#    print(country_code, COUNTRIES[country_code])

