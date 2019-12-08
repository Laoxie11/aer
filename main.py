# -*- coding: UTF-8 -*-
'''
作者：老谢11
邮箱：xz2563842593@163.com
作品介绍：
目前包含答题，录入题目，查看题目三个功能，
尚未完善，接下来的发展方向是加入网络通信建立云题库，以及开发GUI版本
敬请期待接下来的完善！本人水平有限，代码丑陋还请君不要嫌弃！
转载请说明，作者及出处！！！
Author: Lao Xie 11
Email: xz2563842593@163.com
Introduction:
At present, it includes three functions: answering questions, entering questions and viewing questions,
It is not perfect yet. The next development direction is to join the network communication to establish the cloud question bank and develop the GUI version
Please look forward to the next improvement! My level is limited, the code is ugly please don't abandon!
Reprint please explain, author and source!!!
'''
import os

question = []
answer = []
tanswer = []
n = 0
user_history_data = 0
list_long = 0
state = 0

def get_question_answer():
    global question
    global answer
    global tanswer
    global list_long
    f = open('question.txt','r',encoding = 'utf-8')
    get_question = f.read()
    f.close
    i = open('answer.txt','r',encoding = 'utf-8')
    get_answer = i.read()
    i.close
    g = open('tanswer.txt','r',encoding = 'utf-8')
    get_tanswer = g.read()
    g.close
    question = get_question.split()
    answer = get_answer.split()
    tanswer = get_tanswer.split()
    list_long = len(question)

def question_put():
    global state
    put_question = input('请输入要录入的问题:\n')
    ans_a = input('请输入要录入的答案A:\n')
    ans_b = input('请输入要录入的答案B:\n')
    ans_c = input('请输入要录入的答案C:\n')
    ans_d = input('请输入要录入的答案D:\n')
    ans_t = input('请设定正确答案(请用大写字母):\n')
    if put_question and ans_a and ans_b and ans_c and ans_d and ans_t is not '':
        print(f'''
        题目为{ans_a}
        A:{ans_a}
        B:{ans_b}
        C:{ans_c}
        D:{ans_d}
        正确答案为{ans_t}
        ''')
        user_tink = input('确定录入吗？(y/n)')
        if user_tink == 'y':
            f = open('question.txt','a+',encoding = 'utf-8')
            f.write(put_question + os.linesep)
            f.close
            g = open('answer.txt','a+',encoding = 'utf-8')
            g.write(ans_a + os.linesep)
            g.write(ans_b + os.linesep)
            g.write(ans_c + os.linesep)
            g.write(ans_d + os.linesep)
            g.close
            i = open('tanswer.txt','a+',encoding = 'utf-8')
            i.write(ans_t + os.linesep)
            i.close
            state = 1
            os.system('cls')
        elif user_tink == 'n':
            state = 2
            pass
        else:
            print('未知错误！')
    else:
        print('答案或题目不能为空，录入失败！')

def answer_main():
    global question
    global answer
    global tanswer
    global n
    global user_history_data
    user_history_data+=1
    get_question_answer()
    print(f'第{n+1}题：' + question[n])
    print(f'''
    A:{answer[4*n]}
    B:{answer[4*n+1]}
    C:{answer[4*n+2]}
    D:{answer[4*n+3]}
    ''')
    user_choose = input('请选择：')
    if user_choose == tanswer[n]:
        print('恭喜你，回答正确！')
    else:
        print('回答错误！')
    chooseor = input('要继续答题吗？(y/n)')
    if chooseor == 'y':
        if user_history_data == list_long:
            print('没有更多题目了，请联系负责人录入更多题目！')
        else:
            n+=1
            answer_main()
    elif chooseor == 'n':
        pass
    else:
        print('未知错误！')

def look_question():
    global question
    global answer
    get_question_answer()
    print('''
    1.查看所有题目
    2.选择查看
    ''')
    temp = input('请选择：')
    if temp == '1':
        os.system('cls')
        ns = 0
        for i in question:
            print(f'第{ns+1}题：{i}')
            A = answer[4*ns]
            B = answer[4*ns+1]
            C = answer[4*ns+2]
            D = answer[4*ns+3]
            ture_answer = tanswer[ns]
            print(f'A:{A} B:{B} C:{C} D:{D}')
            print(f'答案:{ture_answer}\n')
            ns += 1
        input('按任意继续：')
        os.system('cls')
    elif temp == '2':
        os.system('cls')
        find_question = int(input('请输入查询的题号：'))
        os.system('cls')
        print(f'第{find_question}题：',question[find_question-1])
        A = answer[4]
        B = answer[4*find_question+1]
        C = answer[4*find_question+2]
        D = answer[4*find_question+3]
        print(f'A:{A} B:{B} C:{C} D:{D}')
        ture_answer = tanswer[find_question]
        print(f'答案:{ture_answer}\n')
        input('按任意继续：')

def face():
    print('-' * 30)
    print('''
    1.开始答题
    2.录入题目
    3.查看题目
    ''')
    print('-' * 30)

while True:
    face()
    users = input('请输入功能序号：')
    if users == '1':
        os.system('cls')
        answer_main()
    elif users == '2':
        os.system('cls')
        question_put()
        if state == 1:
            print('录入成功！')
            state = 0
        elif state == 2:
            print('已取消录入！')
            state = 0
    elif users == '3':
        os.system('cls')
        look_question()

    else:
        os.system('cls')
        print('请重试！！！')
