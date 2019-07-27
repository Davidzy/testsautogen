import random

random.seed(100)

def listxzt():
    #选择题是一个15*10的二维数组，
    '''
    [[1,16,31,46,...136],
    [2,17,32,47,...137],
    ...
    [15,30,45,60,...,150]]
    '''
    xzt = [[0]*10 for i in range(15)]
    for j in range(15):
        xzt[j] = [1+j+15*i for i in range(10)]
    return xzt

def listtkt():
    # tkt有20题，每次随机抽取2题
    tkt = [1+i for i in range(20)]
    return tkt

def listydt():
    # ydt[0]有20题，对应前两题，每次抽取2题，ydt[1]有10题，对应第3题，每次抽取1题
    # ydt[2]有10题，对应第4题，每次抽取1题
    ydt = []
    ydt.append([1 + i for i in range(20)])
    ydt.append([21 + i for i in range(10)])
    ydt.append([31 + i for i in range(10)])
    return ydt

def listwst():
    # wst[0]是奇数题号，对应第1题，每次抽取1题，wst[1]是偶数题号，对应第2题，每次抽取1题
    wst = []
    wst.append([2 * i + 1 for i in range(10)])
    wst.append([2 * (i + 1) for i in range(10)])
    return wst

def gen_batch_tests(num_of_tests=5):
    # ids是23*10的数组，对应所有10套模拟题号
    ids = [[] for i in range(num_of_tests)]
    xzt = listxzt()
    tkt = listtkt()
    ydt = listydt()
    wst = listwst()
    # 抽取num_of_tests轮选择题,j是选择题1-15题中第几题
    for j in range(15):
        picked = random.sample(xzt[j], num_of_tests)
        for i in range(num_of_tests):
            ids[i].append(picked.pop())
    # 抽取num_of_tests轮填空题
    picked = random.sample(tkt, 2 * num_of_tests)
    for i in range(num_of_tests):
        for j in range(2):
            ids[i].append(picked.pop())
    # 抽取num_of_tests轮阅读题
    picked12 = random.sample(ydt[0], 2 * num_of_tests)
    picked3 = random.sample(ydt[1], num_of_tests)
    picked4 = random.sample(ydt[2], num_of_tests)
    for i in range(num_of_tests):
        ids[i].append(picked12.pop())
        ids[i].append(picked12.pop())
        ids[i].append(picked3.pop())
        ids[i].append(picked4.pop())
    # 抽取num_of_tests轮完善题
    picked1 = random.sample(wst[0], num_of_tests)
    picked2 = random.sample(wst[1], num_of_tests)
    for i in range(num_of_tests):
        ids[i].append(picked1.pop())
        ids[i].append(picked2.pop())
    for i in range(num_of_tests):
        print(ids[i])
    return ids

ids = gen_batch_tests(5)