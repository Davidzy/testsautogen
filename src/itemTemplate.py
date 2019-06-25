def ch_support():
    retstr = ''
    retstr += '---\n'
    retstr += 'documentclass:\n'
    retstr += '    - ctexart\n'
    retstr += '---\n'
    return retstr


def load_title():
    retstr = ''
    text = '# 全国青少年信息学奥林匹克联赛初赛模拟题'
    retstr += text + '\n'
    return retstr


def first_section_title():
    retstr = ''
    text = '## 一、单项选择题（共10题，每题2分，共计30分；每题有且仅有一个正确选项）'
    retstr += text + '\n'
    return retstr


def second_section_title():
    retstr = ''
    text = '## 二、问题求解（共2题，每题5分，共计10分）'
    retstr += text + '\n'
    return retstr 


def third_section_title():
    retstr = ''
    text = '## 三、阅读程序写结果（共4题，每题8分，共计32分）'
    retstr += text + '\n'
    return retstr 


def fourth_section_title():
    retstr = ''
    text = '## 四、完善程序（共2题，每题14分，共计28分）'
    retstr += text + '\n'
    return retstr 


def fixcode(code):
    code = '```\n' + code + '\n```\n' # markdown code mark
    return code


def emphasize_word(word):
    word = '**' + word + '**'
    return word


def load_first_section_item(item, number):
    '''
    item is an dictionary including
        desc:
        options:
    number is an integer, number of item
    '''
    retstr = ''
    content = item['content'] # description of an item
    line = str(number) + '. ' + content # 题号. 题目描述
    retstr += line + '\n\n'
    if item['code']:
        code = item['code']
        fixed_code = fixcode(code)
        retstr += fixed_code + '\n'
    options = item['options'] # options is an array of options
    cur = ord('A')
    for opt in options:
        # * unordered list + option + dot + option description
        line = '* ' + chr(cur) + '.' + opt # 选项
        retstr += line + '\n'
        cur += 1
    retstr += '\n'
    return retstr


def load_second_section_item(item, number):
    '''
    item is an dictionary including
        desc:
    number is an integer, number of item
    '''
    retstr = ''
    content = item['content'] # description of an item
    line = str(number) + '. ' + content # 题号. 题目描述
    retstr += line + '\n\n'
    return retstr

def load_third_section_item(item, number):
    '''
    item is an dictionary including
        desc:
    number is an integer, number of item
    '''
    retstr = ''
    line = str(number) + '. \n'
    retstr += line
    code = item['code']
    fixed_code = fixcode(code)
    retstr += fixed_code + '\n'
    if len(item['input'])>0:
        line = "输入：" + item['input'] + '\n'
        retstr += line
    line = "输出：\n\n"
    retstr += line
    return retstr


def load_fourth_section_item(item, number):
    '''
    item is an dictionary including
        desc:
    number is an integer, number of item
    '''
    retstr = ''
    emword = emphasize_word(item['title'])
    line = str(number) + '. (' + emword + ')'
    retstr += line
    content = item['content']
    retstr += content + '\n'
    code = item['code']
    fixed_code = fixcode(code)
    retstr += fixed_code + '\n'
    return retstr

def load_first_section_item_with_answer(item, number, answer=False, explain=False):
    '''
    item is an dictionary including
        desc:
        options:
    number is an integer, number of item
    '''
    retstr = ''
    content = item['content'] # description of an item
    line = str(number) + '. ' + content # 题号. 题目描述
    retstr += line + '\n\n'
    try:
        if item['code']:
            code = item['code']
            fixed_code = fixcode(code)
            retstr += fixed_code + '\n'
    except KeyError:
        print(item)
    options = item['options'] # options is an array of options
    cur = ord('A')
    for opt in options:
        # * unordered list + option + dot + option description
        line = '* ' + chr(cur) + '.' + opt # 选项
        retstr += line + '\n'
        cur += 1
    retstr += '\n'
    if answer: #答案开关
        line = emphasize_word('答案') + ': ' # 答案：
        line += item['answer'] + '\n' #答案内容
        retstr += line + '\n'
    if explain: #解释开关
        line = emphasize_word('解释') + ': \n\n'
        retstr += line
        retstr += item['explain'] + '\n\n'
    return retstr


def load_second_section_item_with_answer(item, number, answer=False, explain=False):
    '''
    item is an dictionary including
        desc:
    number is an integer, number of item
    '''
    retstr = ''
    content = item['content'] # description of an item
    line = str(number) + '. ' + content # 题号. 题目描述
    retstr += line + '\n\n'
    if answer: #答案开关
        line = emphasize_word('答案') + ': ' # 答案：
        line += item['answer'] + '\n' #答案内容
        retstr += line + '\n'
    if explain: #解释开关
        line = emphasize_word('解释') + ': \n\n'
        retstr += line
        retstr += item['explain'] + '\n\n'
    return retstr

def load_third_section_item_with_answer(item, number, answer=False, explain=False):
    '''
    item is an dictionary including
        desc:
    number is an integer, number of item
    '''
    retstr = ''
    line = str(number) + '. \n'
    retstr += line
    code = item['code']
    fixed_code = fixcode(code)
    retstr += fixed_code + '\n'
    if len(item['input'])>0:
        line = "输入：" + item['input'] + '\n'
        retstr += line
    line = "输出：\n\n"
    retstr += line
    if answer: #答案开关
        line = emphasize_word('答案') + ': ' # 答案：
        line += item['answer'] + '\n' #答案内容
        retstr += line + '\n'
    if explain: #解释开关
        line = emphasize_word('解释') + ': \n\n'
        retstr += line
        retstr += item['explain'] + '\n\n'
    return retstr


def load_fourth_section_item_with_answer(item, number, answer=False, explain=False):
    '''
    item is an dictionary including
        desc:
    number is an integer, number of item
    '''
    retstr = ''
    emword = emphasize_word(item['title'])
    line = str(number) + '. (' + emword + ')'
    retstr += line
    content = item['content']
    retstr += content + '\n'
    code = item['code']
    fixed_code = fixcode(code)
    retstr += fixed_code + '\n'
    if answer: #答案开关
        line = emphasize_word('答案') + ': ' # 答案：
        line += item['answer'] + '\n' #答案内容
        retstr += line + '\n'
    if explain: #解释开关
        line = emphasize_word('解释') + ': \n\n'
        retstr += line
        retstr += item['explain'] + '\n\n'
    return retstr