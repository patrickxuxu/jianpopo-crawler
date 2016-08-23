import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re

carSeriesError = 'Fatal! Car series not found!'
carCodeError = 'Fatal! Car code not found!'
carBodyError = 'Fatal! Car body not found!'
carTypeError = 'Fatal! Car type not found!'
carPlaceError = 'Fatal! Car place not found!'
carYearError = 'Fatal! Car year not found!'
carMonthError = 'Fatal! Car month not found!'
carEngineError = 'Fatal! Car engine not found!'
carDriveError = 'Fatal! Car drive not found!'


def getPartTable(page):
    tableWrapperPattern = '<table class="table part-table">(.*?)</table>'
    content = re.findall(tableWrapperPattern, page, re.S)
    if(len(content)>0):
        return content

def getTableWrapper(page):
    tableWrapperPattern = '<div class="table-wrapper " >(.*?)</div>'
    content = re.findall(tableWrapperPattern, page, re.S)
    if(len(content)>0):
        return content[0]

def getTr(page):
    trPattern = '<tr.*?>(.*?)</tr>'
    content = re.findall(trPattern, page, re.S)
    if (len(content)>0):
        return content

def getTd(page):
    tdPattern = '<td.*?>(.*?)</td>'
    content = re.findall(tdPattern, page, re.S)
    if(len(content)>0):
        return content

def getContent(page):
    res = []
    tableWrapper = getTableWrapper(page)
    tables = getPartTable(tableWrapper)
    for table in tables:
        trs = getTr(table)
        for tr in trs:
            tds = getTd(tr)
            if(tds!=None):
                if(len(tds)==10 and tds[7]!=None):
                    key = tds[7].encode('utf-8').replace(' ','').replace('\n', '')
                    if(key==''):
                        continue
                    value = tds[2].encode('utf-8')
                    intkey = int(key)
                    res.append([key, value])
    return res

def getItems(page, ulPattern, liPattern, err="Elements not found!"):
    contents = re.findall(ulPattern, page, re.S)
    if(contents==None or len(contents)==0):
        raise Exception(err, page)
    content = contents[0]
    items = re.findall(liPattern, content, re.S)
    if(items==None or len(items)==0):
        raise Exception(err, item)
    return items

def getAdvancedList2(page):
    ulPattern = '<ul class="item-box">(.*?)</ul>'
    liPattern = '<a class="img-link" href="(.*?)">'
    return getItems(page, ulPattern, liPattern, err="Item box not found!")

def getAdvancedList1(page):
    # list all hrefs
    ulPattern = '<ul class="item-box">(.*?)</ul>'
    liPattern = '<a class="img-wrapper" href="(.*?)">'
    return getItems(page, ulPattern, liPattern, err="Item box not found!")

def getCarDrive(page):
    drive_pattern = '<ul class="car-drive".*?>(.*?)</ul>'
    item_pattern = '<li paramName="drive" paramValue="(.*?)".*?</li>'
    return getItems(page, drive_pattern, item_pattern, err=carDriveError)

def getCarEngine(page):
    engine_pattern = '<ul class="car-engine".*?>(.*?)</ul>'
    item_pattern = '<li paramName="engine" paramValue="(.*?)".*?</li>'
    return getItems(page, engine_pattern, item_pattern, err=carEngineError)

def getCarMonth(page):
    month_pattern = '<ul class="car-productMonth".*?>(.*?)</ul>'
    item_pattern = '<li paramName="productMonth" paramValue="(.*?)".*?</li>'
    return getItems(page, month_pattern, item_pattern, err=carMonthError)

def getCarYear(page):
    year_pattern = '<ul class="car-productYear".*?>(.*?)</ul>'
    item_pattern = '<li paramName="productYear" paramValue="(.*?)".*?</li>'
    return getItems(page, year_pattern, item_pattern, err=carYearError)

def getCarPlace(page):
    place_pattern = '<ul class="car-place".*?>(.*?)</ul>'
    item_pattern = '<li paramName="region" paramValue="(.*?)".*?</li>'
    return getItems(page, place_pattern, item_pattern, err=carPlaceError)

def getCarType(page):
    type_pattern = '<ul class="car-type".*?>(.*?)</ul>'
    item_pattern = '<li paramName="model" paramValue="(.*?)".*?</li>'
    return getItems(page, type_pattern, item_pattern, err=carTypeError)

def getCarBody(page):
    body_pattern = '<ul class="car-body".*?>(.*?)</ul>'
    item_pattern = '<li paramName="body" paramValue="(.*?)".*?</li>'
    return getItems(page, body_pattern, item_pattern, err=carBodyError)

def getCarCode(page):
    code_pattern = '<ul class="car-code".*?>(.*?)</ul>'
    item_pattern = '<li paramName="code" paramValue="(.*?)".*?</li>'
    return getItems(page, code_pattern, item_pattern, err=carCodeError)

def getCarSeries(page):
    series_pattern = '<ul class="car-series".*?>(.*?)</ul>'
    item_pattern = '<li paramName="series" paramValue="(.*?)".*?</li>'
    return getItems(page, series_pattern, item_pattern, err=carSeriesError)

if __name__ == '__main__':
    raise Exception("Should not lauch process here!")
