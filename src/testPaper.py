class TestPaper:
    testconfig = {'t1number':0, 't2number':20, 't3number':0, 't4number':0}
    # testconfig = {'t1number':10, 't2number':2, 't3number':4, 't4number':2}
    def __init__(self, totallist):
        self.t1list = []
        self.t2list = []
        self.t3list = []
        self.t4list = []
        for idx in range(len(totallist)):
            if(len(self.t1list)<self.testconfig['t1number']): self.t1list.append('xz'+str(totallist[idx]))
            elif(len(self.t2list)<self.testconfig['t2number']): self.t2list.append('tk'+str(totallist[idx]))
            elif(len(self.t3list)<self.testconfig['t3number']): self.t3list.append('yd'+str(totallist[idx]))
            elif(len(self.t4list)<self.testconfig['t4number']): self.t4list.append('ws'+str(totallist[idx]))

    def get_t1(self):
        return self.t1list
    
    def get_t2(self):
        return self.t2list

    def get_t3(self):
        return self.t3list

    def get_t4(self):
        return self.t4list

    def print_shijuan(self):
        print('一、选择题')
        for item in self.t1list:
            print(item, sep=', ')
        print()
        print('二、填空题')
        for item in self.t2list:
            print(item, sep=', ')
        print()
        print('三、程序题')
        for item in self.t3list:
            print(item, sep=', ')
        print()
        print('四、完善程序')
        for item in self.t4list:
            print(item, sep=', ')
        print()




if __name__ == '__main__':
    papers = [
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        # [1,2,3,4,5,6,7,8,9,10,1,2,1,2,3,4,1,2],
        # [16,17,18,19,20,21,22,23,24,25,3,4,5,6,7,8,3,4]
    ]
    shijuan = []
    for paper in papers:
        shijuan.append(TestPaper(paper))
    
    for sj in shijuan:
        sj.print_shijuan()
