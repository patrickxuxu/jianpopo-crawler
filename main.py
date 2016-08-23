import copy
import sys

import send_request as sr
import get_elements as ge

base_url = 'http://www.jianpopo.com/vehicle/advancedSearch.html'
list_url = 'http://www.jianpopo.com/vehicle/'

knownKeys = []

filePath = 'result_all.dat'

def writeFile(contents):
    writer = open(filePath, 'a')
    for content in contents:
        try:
            writer.write(content+"\n")
        except Exception as e:
            print e
    writer.close()

def getContent(drive, params):
    params = copy.deepcopy(params)
    params['drive'] = drive
    response = sr.getRequest(base_url, params=params)
    page = response[2]
    items1 = ge.getAdvancedList1(page)
    for item1 in items1:
        url = list_url + item1
        result1 = sr.getRequest(url)[2]
        items2 = ge.getAdvancedList2(result1)
        for item2 in items2:
            finalUrl = list_url + item2
            result2 = sr.getRequest(finalUrl)[2]
            if(result2==None or result2==''):
                continue
            try:
                res = ge.getContent(result2)
                resset = []
                for elem in res:
                    # if(elem[0] not in knownKeys):
                    knownKeys.append(elem[0])
                    raw = elem[0]+": "+ elem[1]
                    resset.append(raw)
                writeFile(resset)
            except Exception as e:
                print e

def getDrives(engine, params):
    params = copy.deepcopy(params)
    params['engine'] = engine
    page = sr.getRequest(base_url, params=params)[2]
    drives = ge.getCarDrive(page)
    for drive in drives:
        getContent(drive, params)

def getEngines(month, params):
    params = copy.deepcopy(params)
    params['productMonth'] = month
    page = sr.getRequest(base_url, params=params)[2]
    engines = ge.getCarEngine(page)
    for engine in engines:
        getDrives(engine, params)

def getMonths(year, params):
    params = copy.deepcopy(params)
    params['productYear'] = year
    page = sr.getRequest(base_url, params=params)[2]
    months = ge.getCarMonth(page)
    for month in months:
        getEngines(month, params)

def getYears(place, params):
    params = copy.deepcopy(params)
    params['region'] = place
    page = sr.getRequest(base_url, params=params)[2]
    years = ge.getCarYear(page)
    for year in years:
        getMonths(year, params)

def getPlaces(typee, params):
    print("\t\t\tgetting type %s" % typee)
    params = copy.deepcopy(params)
    params['model'] = typee
    page = sr.getRequest(base_url, params=params)[2]
    places = ge.getCarPlace(page)
    for place in places:
        getYears(place, params)

def getTypes(body, params):
    print("\t\tgetting body %s" % body)
    params = copy.deepcopy(params)
    params['body'] = body
    page = sr.getRequest(base_url, params=params)[2]
    types = ge.getCarType(page)
    for typee in types:
        getPlaces(typee, params)

def getBodies(code, params):
    print("\tgetting code %s" % code)
    params = copy.deepcopy(params)
    params['code'] = code
    page = sr.getRequest(base_url, params=params)[2]
    bodies = ge.getCarBody(page)
    for body in bodies:
        getTypes(body, params)

def getCodes(series):
    print("getting series %s" % series)
    params = {'series': series}
    response = sr.getRequest(base_url, params=params)
    page = response[2]
    codes = ge.getCarCode(page)
    for code in codes:
        getBodies(code, params)

def getSeries():
    response = sr.getRequest(base_url)
    page = response[2]
    seriess = ge.getCarSeries(page)
    for series in seriess:
        getCodes(series)

def main():
    sys.stdout = open("stdout", "w")
    getSeries()

if __name__ == '__main__':
    main()
