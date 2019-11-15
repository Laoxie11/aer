import os
import re
question = 0
answer = 0
def question_put():
    put_question = input(':')
    ans_a = input('A:')
    ans_b = input('B:')
    ans_c = input('C:')
    ans_d = input('D:')
    f = open('question.txt','a+',encoding = 'utf-8')
    f.write(put_question + os.linesep)
    f.close
    g = open('answer.txt','a+',encoding = 'utf-8')
    g.write(ans_a + os.linesep)
    g.write(ans_b + os.linesep)
    g.write(ans_c + os.linesep)
    g.write(ans_d + os.linesep)
    g.close
    print('Hi')
def get_question_answer():
    global question
    global answer
    f = open('question.txt','r',encoding = 'utf-8')
    get_question = f.read()
    f.close
    i = open('answer.txt','r',encoding = 'utf-8')
    get_answer = i.read()
    i.close
    question = get_question.split()
    answer = get_answer.split()
    print(question)
    print(answer)
question_put()
get_question_answer()
