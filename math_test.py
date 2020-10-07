
# -*- coding:utf-8 -*-  
  
#os模块中包含很多操作文件和目录的函数  
import os
import sys
import re
import random
import time

print ("整数口算测验 by 慕慕大昭爸爸\n")

rule = ["加", "减", "乘", "除"]

num_rule = 0
bool_allNeg = False
bool_numOnly = False
num_max = 0
num_mode = 0
arrstr_yes = ["Y", "y", "Yes", "yes"]
arrstr_question = []
arrnum_result = []
arrnum_ans = []
arrnum_rating = []
str_output_exam = 'exam_list_' + (time.strftime("%Y_%m_%d_%H_%M", time.localtime())) + '.txt'
str_output_answer = 'exam_answer_' + (time.strftime("%Y_%m_%d_%H_%M", time.localtime())) + '.txt'


n = 0
while n < 4:
    str_rule = input("需要" + rule[n] + "法吗，Y、y、Yes、yes表示要，其他不要？输入：")
    if str_rule in arrstr_yes:
        num_rule += 2 ** n
    n += 1
if num_rule == 0:
    input ("什么都不做那来干啥，请按Return（Enter）退出...")
    exit()
    
if num_rule & 1:
    str_rule = input("减法的结果允许出现负数吗，Y、y、Yes、yes表示允许，其他不允许？输入：")
    if str_rule in arrstr_yes:
        bool_allNeg = True
    else:
        bool_allNeg = False
        
if num_rule & 12:
    str_rule = input("乘法的乘数、被乘数，或者除法的除数限制1位数吗，Y、y、Yes、yes表示限制，其他不限制？输入：")
    if str_rule in arrstr_yes:
        bool_numOnly = True
    else:
        bool_numOnly = False


try: 
    while (True):
        str_max = input("绝对值在多少以内（接受10到10000），默认30：")
        if int(str_max) < 10 or int(str_max) > 10000 :
            print ("范围超过啦！")
        else :
            num_max = int(str_max)
            break
except:
    num_max = 30
    print ("输入不是数字，因此范围设置为默认30")
        
try:
    while (True):
        str_amount = input("做几道题（接受1到100），默认10：")
        if int(str_amount) < 1 or int(str_amount) > 100:
            print ("范围超过啦！")
        else:
            num_amount = int(str_amount)
            break
except:
    num_amount = 10
    print ("输入不是数字，因此数量设置为默认10")   
    
try:        
    while (True):
        str_mode = input("测试模式：[1]输出题目到结果；[2]在电脑上一题题练习；[3]考试模式 默认[1]，请输入数字：")
        if int(str_mode) < 1 or int(str_mode) > 3 :
            print ("没有这个选项")
        else :
            num_mode = int(str_mode)
            break
except:
    num_mode = 1
    print ("输入不是数字，因此默认输出题目到文件")   
    
rule_out = "\n这次需要绝对值在" + str(num_max) + "以内的"
n = 0
while n < 4:
    if num_rule & 2 ** n:
        rule_out = rule_out + rule[n]
    n += 1
rule_out = rule_out + "法" + str(num_amount) + "题。\n"
if num_rule & 12:
    if bool_numOnly:
        rule_out = rule_out + "乘法的乘数、被乘数，或者除法的除数限制1位数。\n"
    else:
        rule_out = rule_out + "乘法的乘数、被乘数，或者除法的除数不限制1位数。\n"
        
if num_rule & 1:
    if bool_allNeg:
        rule_out = rule_out + "减法的结果允许出现负数。"
    else:
        rule_out = rule_out + "减法的结果不允许出现负数。"
if (num_mode == 1):
    rule_out = rule_out + "测试题将会被输出到结果文件。"
elif (num_mode == 2):
    rule_out = rule_out + "测试题将在电脑上一题题练习，最后结果会被输出到结果文件。\n"
else:
    rule_out = rule_out + "进入考试模式，最后结果会被输出到结果文件。"
print(rule_out)


#打开文件 
file_output_exam = open(str_output_exam,'w',encoding='utf-8')
file_output_answer = open(str_output_answer,'w',encoding='utf-8')


n = 0


while n < num_amount:
    #锚定一个在测试范围内运算符
    while (True):
        num_operator = random.randint(0, 3)
        if num_operator < 4 and 2 ** num_operator & num_rule:
            break
    
    #确定运算符后，找前后变量直到题目结果为范围内的整数
    while (True):
        num_a = random.randint(1, num_max)
        num_b = random.randint(1, num_max)
        # 根据慕慕同学的要求，运算数字中不再出现0
        if num_operator == 0:
            if num_a + num_b <= num_max:
                #加法，判断和不超过最大值
                arrstr_question.append(str(num_a) + "\t＋\t" + str(num_b) + "\t＝\t")
                arrnum_result.append(num_a + num_b)
                break
        elif num_operator == 1:
            if num_a >= num_b or bool_allNeg:
                #减法，判断差为非负数，或者允许负数就不管了
                arrstr_question.append(str(num_a) + "\t－\t" + str(num_b) + "\t＝\t") 
                arrnum_result.append(num_a - num_b)
                break
        elif num_operator == 2:
            if ((bool_numOnly and num_a < 10 and num_b < 10) or (not bool_numOnly)) and num_a * num_b <= num_max:
                #乘法，判断是否限制1位数乘法，再判断乘积是否超范围，都符合就ok
                arrstr_question.append(str(num_a) + "\t×\t" + str(num_b) + "\t＝\t") 
                arrnum_result.append(num_a * num_b)
                break
        elif num_operator ==3:
            if (num_b > 1) and ((bool_numOnly and num_b < 10) or (not bool_numOnly)) and num_a > 1 and num_a * num_b <= num_max:
                num_a = num_a * num_b
                #除法，除数不为0、是否限制除数为1位数，确保整除，都符合就ok
                arrstr_question.append(str(num_a) + "\t÷\t" + str(num_b) + "\t＝\t")
                arrnum_result.append(int(num_a / num_b))
                break
        else:
           break
    #print (arrstr_question[n], arrnum_result[n])
    file_output_answer.writelines(arrstr_question[n] + str(arrnum_result[n]) + "\n")
    if num_mode == 1:
        print(arrstr_question[n])
        file_output_exam.writelines(arrstr_question[n] + "\n")
    else:
        # 电脑模式下接受用户输入的答案
        answered = False
        while(not answered):
            try:
                answer_try = int(input(arrstr_question[n]))
                answered = True
            except:
                print("请输入计算结果数字后再按return/enter键哦。")
        # 防止输入错误的bug
        arrnum_ans.append(answer_try)
        arrnum_rating.append(0)
        #练习模式下记录题目并实时反馈结果
        if num_mode == 2:
            while arrnum_result[n] != arrnum_ans[n]:
                print("做错啦！")
                # 慕慕说不要“再想一想”
                #记录答错次数
                arrnum_rating[n] += 1
                #删除输入值
                arrnum_ans.pop(n)
                arrnum_ans.append(int(input(arrstr_question[n])))
            if arrnum_rating[n] > 0:
                str_desc = "\t做错" + str(arrnum_rating[n]) + "次后做对"
                print("这道题做错了" + str(arrnum_rating[n]) + "次之后才做对哦")
            else:
                str_desc = "\t回答正确！"
                print("回答正确！")
            file_output_exam.writelines(arrstr_question[n] + str_desc + "\n")
        elif num_mode == 3:
            #考试模式记录题目、作答结果以及判断
            if arrnum_result[n] != arrnum_ans[n]:
                arrnum_rating[n] += 1
                str_desc = "\t错误！"
            else:
                str_desc = "\t正确！"
            file_output_exam.writelines(arrstr_question[n] + str(arrnum_ans[n]) + str_desc + "\n")   
    n += 1

file_output_exam.close()
file_output_answer.close()

if num_mode == 1:
    print("请打开" + str_output_exam + "打印本次测试题目")
    print("请打开" + str_output_answer + "打印本次测试答案")
elif num_mode == 2:
    print("请打开" + str_output_exam + "打印本次测试题目和作答情况")
    print("请打开" + str_output_answer + "打印本次测试答案")
elif num_mode == 3:
    if sum(arrnum_rating) == 0:
        print("太棒了！全对！本次测试100分！")
    else:
        print("好可惜，错了" + str(sum(arrnum_rating)) + "题，本次测试" + str(100 * (1 - sum(arrnum_rating) / len(arrnum_rating))) + "分")
    print("请打开" + str_output_exam + "打印本次测试题目和作答情况")
    print("请打开" + str_output_answer + "打印本次测试答案")
    
input("按Return（Enter）键结束...")

#关闭文件  
