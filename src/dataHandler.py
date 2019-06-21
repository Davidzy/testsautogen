import json
import codecs

def fetch_data():
    xzfile = '../data/xzt.json'
    tkfile = '../data/tkt.json'
    ydfile = '../data/ydt.json'
    wsfile = '../data/wst.json'
    testdata = {}
    # fetch data from json file
    with open(xzfile, 'r', encoding='utf-8') as f:
        xzt = json.load(f)
        testdata['xzt'] = xzt
    with open(tkfile, 'r', encoding='utf-8') as f:
        tkt = json.load(f)
        testdata['tkt'] = tkt
    with open(ydfile, 'r', encoding='utf-8') as f:
        ydt = json.load(f)
        testdata['ydt'] = ydt
    with codecs.open(wsfile, 'r', 'utf-8-sig') as f:  
    # with open(wsfile, 'r', encoding='utf-8') as f:
        wst = json.load(f)
        testdata['wst'] = wst
    return testdata

def handlet1(shijuan, itembank):
    retdata = []
    itemids = shijuan.get_t1()
    idset = set(itemids)
    for item in itembank['xzt']:
        if item['id'] in idset:
            retdata.append(item)
    return retdata

def handlet2(shijuan, itembank):
    retdata = []
    itemids = shijuan.get_t2()
    idset = set(itemids)
    for item in itembank['tkt']:
        if item['id'] in idset:
            retdata.append(item)    
    return retdata

def handlet3(shijuan, itembank):
    retdata = []
    itemids = shijuan.get_t3()
    idset = set(itemids)
    for item in itembank['ydt']:
        if item['id'] in idset:
            retdata.append(item)    
    return retdata

def handlet4(shijuan, itembank):
    retdata = []
    itemids = shijuan.get_t4()
    idset = set(itemids)
    for item in itembank['wst']:
        if item['id'] in idset:
            retdata.append(item)    
    return retdata


def gen_all_items():
    t1 = [x for x in range(1,151)]
    t2 = [x for x in range(1,21)]
    t3 = [x for x in range(1,41)]
    t4 = [x for x in range(1,21)]
    data = t1 + t2 + t3 + t4
    return data