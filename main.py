
import re
import os
n = 0
answers = []
def face():
    print('#' * 30)
    print(
    """
    1.题目录入
    2.答题
    """
    )
    print('#' * 30)
def add_ques():
    pass
def add_ans():
    aa = input('请录入答案A:')
    ba = input('请录入答案B:')
    ca = input('请录入答案C:')
    da = input('请录入答案D:')
    answer = {"A":aa,"B":ba,"C":ca,"D":da}
    answers.append(answer)
def str_gll():
    global answers
    answersnel = str(answers)
    r='[’!"#$%&\'()*+-./;<=>?@[\\]^_`{|}~]+'
    line=re.sub(r,'',answersnel)
    print(line)
while True:
    face()
    user_choose = input("请输入功能序号:")
    os.system("clear")
    if user_choose == '1':
        add_ans()
        str_gll()
    elif user_choose == '2':
        print('World')
    #未完工~~~
