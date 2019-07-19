import itemTemplate as it
import dataHandler as dh
from testPaper import TestPaper
from testPaper import papers_list

def load_title():
    title = it.load_title()
    return title

def load_first_section(items):
    '''
    item data is an array of item object(dictionary)
    '''
    retstr = ''
    title = it.first_section_title()
    retstr += title + '\n'
    order = 1 # number of item
    for item in items:
        itemtxt = it.load_first_section_item_with_answer(item, order, answer=True, explain=True)
        retstr += itemtxt
        order += 1
    return retstr
    
def load_second_section(items):
    '''
    '''
    retstr = ''
    title = it.second_section_title()
    retstr += title + '\n'
    order = 1
    for item in items:
        itemtxt = it.load_second_section_item_with_answer(item, order, answer=True, explain=True)
        retstr += itemtxt
        order += 1
    return retstr
    
def load_third_section(items):
    '''
    '''
    retstr = ''
    title = it.third_section_title()
    retstr += title + '\n'
    order = 1
    for item in items:
        itemtxt = it.load_third_section_item_with_answer(item, order, answer=True, explain=True)
        retstr += itemtxt
        order += 1
    return retstr
    
def load_fourth_section(items):
    '''
    '''
    retstr = ''
    title = it.fourth_section_title()
    retstr += title + '\n'
    order = 1
    for item in items:
        itemtxt = it.load_fourth_section_item_with_answer(item, order, answer=True, explain=True)
        retstr += itemtxt
        order += 1
    return retstr
    
def write_test_to_md(shijuan, data, fout):
    #加载markdown to tex中文支持
    cstext = it.ch_support()
    print(cstext, file=fout)
    #加载试卷标题
    title = load_title()
    print(title, file=fout)
    #加载第一题
    testData = dh.handlet1(shijuan, data)
    text1 = load_first_section(testData)
    print(text1, file=fout)
    #加载第二题
    testData = dh.handlet2(shijuan, data)
    text2 = load_second_section(testData)
    print(text2, file=fout)
    #加载第三题
    testData = dh.handlet3(shijuan, data)
    text3 = load_third_section(testData)
    print(text3, file=fout)
    #加载第四题
    testData = dh.handlet4(shijuan, data)
    text4 = load_fourth_section(testData)
    print(text4, file=fout)


if __name__ == '__main__':
#    papers = [dh.gen_all_items()]
    papers = papers_list
    itembank = dh.fetch_data()
    shijuan = []
    count = 1
    for paper in papers:
        shijuan.append(TestPaper(paper))
        filename = '../Doc/moniti'+str(count)+'_ans.md'
        with open(filename, 'w+', encoding='utf8') as fout:
            write_test_to_md(shijuan[count-1], itembank, fout)
        count+=1
