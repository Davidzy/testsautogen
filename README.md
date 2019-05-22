#Test auto generation
##Folders
reference: some reference document including markdown syntax, vscode shortcuts, and etc.
##Doc
Markdown documents


##试题格式
为试题设计属性
id: 试题的唯一标识。xz1,tk1,ws1,yd1，xz表示选择，tk表示填空，ws表示完善程序，yd表示阅读程序。序号从1开始按顺序编号。
content: 字符串，试题的内容，题面描述
options: 选择题的选项，为列表格式，每一项是字符串
answer：字符串，答案，选择题就是ABCD，填空题就是所有空的答案，完善程序就是所有空的答案
explain: 字符串，试题的详细版文字解释
imgurl: 字符串或NULL题目图片的网址
soundurl: 字符串或NULL，试题音频解说的网址
code: 字符串，题目代码