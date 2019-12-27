import wptools
from datetime import datetime, date
import pickle
from object_data import nextnams, params


RESULT_PICKLE_FILENAME = "solsysbod_add_dct.pickle"

def getPage(objname):
    page = wptools.page(objname)
    page.get_query()
    page.get_parse()
    return page

def getParam(page, param):
    '''Get parameter from infobox'''
    return page.data['infobox'].get(param)

def getDate(page):
    try:
        dateDisc = page.data['infobox'].get('discovered')
        if not dateDisc:
            dateDisc = page.data['infobox'].get('discovery_date')
        if dateDisc:
            dateObj = parseDate(dateDisc)
        else:
            dateObj = dateDisc
    except AttributeError:
        dateObj = None
    try:
        date_str = dateObj.strftime("%d.%m.%Y")
    except AttributeError:
        date_str = dateObj
    return date_str

def parseDate(dateDisc):
    if "," in dateDisc and len(dateDisc.split()) == 3:
        try:
            dateProperDisc = datetime.strptime(dateDisc, "%B %d, %Y")
        except ValueError:
            dateProperDisc = dateDisc
    elif "," in dateDisc and len(dateDisc.split()) == 2:
        try:
            dateProperDisc = datetime.strptime(dateDisc, "%B, %Y")
        except ValueError:
            dateProperDisc = dateDisc
    elif "," not in dateDisc and len(dateDisc.split()) == 3:
        try:
            dateProperDisc = datetime.strptime(dateDisc, "%d %B %Y")
        except ValueError:
            dateProperDisc = dateDisc
    elif len(dateDisc.split()) == 1:
        dateProperDisc = dateDisc
    else:
        print("No way to parse data:", dateDisc)
        dateProperDisc = dateDisc
    return dateProperDisc

bodies_params_dct = {}
for objname in nextnams:
    page = getPage(objname)
    if page.get('infobox'):
        date_str = getDate(page)
        gparams = {'discovery_date': date_str}
        for param in params:
            try:
                gparams[param] = getParam(page, param)
            except AttributeError:
                gparams[param] = None
        bodies_params_dct[objname] = gparams
    else:
        print(f'\nNo infobox for {objname}!\n')

print(f"{len(bodies_params_dct)} objects")

with open(RESULT_PICKLE_FILENAME, 'wb') as handle:
    pickle.dump(bodies_params_dct, handle)
