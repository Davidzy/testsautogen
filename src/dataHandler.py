import json

def fetch_data():
    xzfile = '../data/xz.json'
    tkfile = '../data/tk.json'
    ydfile = '../data/yd.json'
    wsfile = '../data/ws.json'
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
    with open(wsfile, 'r', encoding='utf-8') as f:
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