class TestPaper:
#    testconfig = {'t1number':150, 't2number':20, 't3number':40, 't4number':20} #gen all items in one paper
    testconfig = {'t1number':15, 't2number':2, 't3number':4, 't4number':2} #gen standard paper
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

papers_list = [
        

[16, 47, 108, 109, 140, 6, 97, 38, 39, 55, 11, 12, 28, 14, 120, 16, 3, 11, 19, 28, 38, 7, 2],
[91, 122, 48, 124, 125, 141, 37, 113, 114, 145, 86, 42, 118, 29, 135, 5, 6, 5, 20, 25, 39, 11, 18],
[61, 2, 3, 79, 35, 111, 112, 53, 9, 85, 26, 57, 103, 119, 30, 14, 9, 4, 17, 26, 40, 15, 10],
[106, 107, 78, 19, 20, 126, 127, 68, 84, 100, 56, 147, 13, 74, 105, 8, 15, 16, 8, 27, 35, 13, 20],
[31, 137, 93, 64, 110, 21, 142, 143, 69, 25, 131, 27, 148, 149, 75, 1, 12, 18, 15, 30, 32, 9, 6],
[46, 62, 33, 4, 95, 96, 52, 8, 129, 130, 41, 117, 133, 134, 15, 10, 2, 7, 2, 21, 34, 17, 12],
[1, 32, 123, 34, 80, 51, 82, 98, 54, 70, 101, 87, 88, 104, 45, 13, 4, 13, 1, 22, 37, 19, 4],
[121, 77, 18, 94, 50, 81, 67, 83, 24, 10, 71, 72, 58, 59, 150, 19, 17, 6, 3, 29, 36, 3, 8],
[76, 92, 138, 49, 65, 36, 7, 23, 99, 115, 146, 102, 43, 89, 60, 20, 7, 14, 10, 23, 31, 1, 16],
[136, 17, 63, 139, 5, 66, 22, 128, 144, 40, 116, 132, 73, 44, 90, 11, 18, 12, 9, 24, 33, 5, 14]
        ]

if __name__ == '__main__':
    papers = [
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        # [1,2,3,4,5,6,7,8,9,10,1,2,1,2,3,4,1,2],
        # [16,17,18,19,20,21,22,23,24,25,3,4,5,6,7,8,3,4]
    ]
    shijuan = []
    for paper in papers:
        shijuan.append(TestPaper(paper))
    
    for sj in shijuan:
        sj.print_shijuan()
