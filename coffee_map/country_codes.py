from pygal_maps_world.i18n import COUNTRIES
#from pygal.i18n import COUNTRIES

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    
    if country_name == 'Tanzania':
        icode = 'tz'
        return icode
    if country_name == 'Venezuela':
        icode = 've'
        return icode
    if country_name == 'Bolivia':
        icode = 'bo'
        return icode

    return None

#print(get_country_code('Andorra'))
#print(get_country_code('United Arab Emirates'))
#print(get_country_code('Afghanistan'))
