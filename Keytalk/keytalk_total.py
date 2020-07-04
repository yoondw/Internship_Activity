#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:43:36 2020

@author: 윤도원
"""


import pandas as pd
import random
from pronounciation_rules import pro_rules
from unicode import join_jamos_char
from konlpy.tag import Kkma

def word_concat(meta_list, filter_list):
    meta_randint = random.randint(0, len(meta_list) - 1)
    meta_word = meta_list[meta_randint]
    
    filter_randint_list = random.sample(range(len(filter_list) - 1), 2)
    filter_word1 = filter_list[filter_randint_list[0]]
    filter_word2 = filter_list[filter_randint_list[1]]
    
    return filter_word1, meta_word, filter_word2

def word_concat_no_meta(filter_list):
    filter_randint_list = random.sample(range(len(filter_list) - 1), 2)
    filter_word1 = filter_list[filter_randint_list[0]]
    filter_word2 = filter_list[filter_randint_list[1]]
    
    return filter_word1, filter_word2

def get_expression(category):
    if category == '구성내용':
        return ['아주', '제법', '대박', '사뭇', '무척', '언제나 그렇듯', '퍽']
    elif category == '그림체':
        return ['아주', '제법', '사뭇', '대박', '짱', '무척', '약간', '퍽', '쌉']
    elif category == '독자 반응':
        return ['아주', '제법', '막', '사뭇', '대박', '무척', '언제나 그렇듯', '퍽', '줄곧']
    elif category == '분위기':
        return ['아주', '막', '제법', '사뭇', '대박', '짱', '좀', '무척', '약간', '언제나 그렇듯', '퍽', '쌉', '줄곧', '확']
    elif category == '스토리':
        return ['아주', '막', '제법', '사뭇', '대박', '짱', '좀', '무척', '약간', '언제나 그렇듯', '퍽']
    elif category == '시청자 반응':
        return ['아주', '막', '제법', '사뭇', '대박', '짱', '무척', '약간', '언제나 그렇듯', '줄곧', '쌉']
    elif category == '출연진':
        return ['아주', '제법', '사뭇', '대박', '짱', '좀', '무척', '언제나 그렇듯', '줄곧']
    elif category == '캐릭터':
        return ['아주', '제법', '사뭇', '대박', '짱', '좀', '무척', '언제나 그렇듯', '퍽', '쌉', '줄곧']
    else:
        return ['아주', '제법', '사뭇', '대박']
    
def korean_split(korean_word):

    r_lst = []
    for w in list(korean_word.strip()):
        ## 영어인 경우 구분해서 작성함. 
        if '가'<=w<='힣':
            ## 588개 마다 초성이 바뀜. 
            ch1 = (ord(w) - ord('가'))//588
            ## 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
        else:
            r_lst.append([w])
    return r_lst

def rule1(text):
    '한국 인기많은 비율좋은 방송'
    bulpha = ['ㅊ', 'ㅆ', 'ㄾ', 'ㄻ', 'ㄽ', 'ㄲ', 'ㅂ', 'ㄿ', 'ㅋ', 'ㄼ', 'ㄶ', 'ㄳ', 'ㄺ', 'ㅌ', 'ㅀ', 'ㅈ', 'ㅍ', 'ㄵ', 'ㄷ', 'ㅅ', 'ㄱ', 'ㅄ']
    pyeong = ['ㄱ', 'ㄷ', 'ㅂ', 'ㅅ', 'ㅈ']
    splited_kor = korean_split(text)
    for i in range(len(splited_kor) - 1):
        # 받침이 불파음화라면
        if splited_kor[i][-1] in bulpha:
            if splited_kor[i+1][0] in pyeong:
                # print(splited_kor[i][-1])
                # print(splited_kor[i+1][0])
                return True
        else:
            return False
        
def rule2(text):
    payeol = ['ㄱ', 'ㄷ', 'ㅂ']
    biyeom = ['ㅁ', 'ㄴ']
    splited_kor = korean_split(text)
    for i in range(len(splited_kor) - 1):
        # 받침이 파열음이라면
        if splited_kor[i][-1] in payeol:
            # 만약 자음이 비염이라면
            if splited_kor[i+1][0] in biyeom:
#                 print(splited_kor[i][-1])
#                 print(splited_kor[i+1][0])
                return True
    return False

def rule3(text):
    payeol = ['ㄱ', 'ㄷ', 'ㅂ']
    pachal = ['ㅈ']
    splited_kor = korean_split(text)
    for i in range(len(splited_kor) - 1):
        # 받침이 파열음이거나 파찰음이라면
        if splited_kor[i][-1] in payeol or splited_kor[i][-1] in pachal:
            # 자음이 'ㅎ'이라면
            if splited_kor[i+1][0] == 'ㅎ':
#                 print(splited_kor[i][-1])
#                 print(splited_kor[i+1][0])
                return True
    return False

def rule4(text):
    bakchim = ('ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅄ ㅅ ㅆ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ'.split())
    splited_kor = korean_split(text)
    for i in range(len(splited_kor) - 1):
        # 은/는으로 시작된다면
        if text[i] == '은' or text[i] == '는' or text[i] == '한':
            # 앞의 자음이 ㅇ으로 시작되고 받침이 있다면
            if splited_kor[i+1][0] == 'ㅇ' and splited_kor[i+1][-1] != ' ':
                pass
        # 받침이 있다면
        elif splited_kor[i][-1] in bakchim:
            # 'ㅇ'으로 시작된다면
            if splited_kor[i+1][0] == 'ㅇ':
#                 print(splited_kor[i][-1])
#                 print(splited_kor[i+1][0])
                return True
    return False

def rule5(text):
    splited_kor = korean_split(text)
    for i in range(len(splited_kor) - 1):
        # 받침이 ㄹ 이라면
        if splited_kor[i][-1] in 'ㄹ':
            # 'ㄴ'으로 시작된다면
            if splited_kor[i+1][0] == 'ㄴ':
#                 print(splited_kor[i][-1])
#                 print(splited_kor[i+1][0])
                return True
    return False

def get_error(*args):
    token = True
    
#     lists = []
    
#     lists.append(expression)
#     lists.append(filter1)
#     lists.append(meta_connection)
#     lists.append(filter2)
#     lists.append(category)
    
    lists = list(args)
#     print(lists)
    
    
    for i in range(len(lists) - 1):
        if rule1(lists[i][-1] + lists[i + 1][0]) == False:
            if rule2(lists[i][-1] + lists[i + 1][0]) == False:
                if rule3(lists[i][-1] + lists[i + 1][0]) == False:
                    if rule4(lists[i][-1] + lists[i + 1][0]) == False:
                        if rule5(lists[i][-1] + lists[i + 1][0]) == False:
                            pass
                        else:
                            token = False
#                             print('err 5 : ', lists[i][-1] + lists[i + 1][0])
                    else:
                        token = False
#                         print('err 4 : ', lists[i][-1] + lists[i + 1][0])
                else:
                    token = False
#                     print('err 3 : ', lists[i][-1] + lists[i + 1][0])
            else:
                token = False
#                 print('err 2 : ', lists[i][-1] + lists[i + 1][0])
        else:
            token = False
#             print('err 1 : ', lists[i][-1] + lists[i + 1][0])
    return token

def filter_connection(filter1):
    kkma = Kkma()
    
    div = kkma.pos(filter1)
    
    for i in range(len(div)):
        if div[i][-1] == 'ECS':
            return filter1 + ' 그리고'
    
    go_list = []

    if len(div) == 2 and (div[0][-1] == 'VV' or div[0][-1] == 'VA') and (div[-1][0] == '는' or div[-1][0] == '은'):
        for j in range(len(div) - 1):
            go_list.append(div[j][0])
        go_list.append('고')
    elif len(div) > 1 and (div[-1][0] == 'ㄴ' or div[-1][0] == '는') and div[-2][0] == '하':
        for j in range(len(div) - 1):
            go_list.append(div[j][0])
        go_list.append('고')
    elif len(div) == 3 and div[0][-1] == 'NNG' and div[1][0] == '이' and div[-1][0] == 'ㄴ':
        for j in range(len(div) - 1):
            go_list.append(div[j][0])
        go_list.append('고')
    elif len(div) == 2 and div[0][-1] == 'VA' and div[-1][0] == 'ㄴ':
        for j in range(len(div) - 1):
            go_list.append(div[j][0])
        go_list.append('고') 
    elif len(div) > 1 and div[-2][-1] == 'XSA' and div[-1][0] == 'ㄴ':
        for j in range(len(div) - 1):
            go_list.append(div[j][0])
        go_list.append('고')
    elif div[-1][-1] == 'MDN' and div[-1][0] == '한':
        for j in range(len(div) - 1):
            go_list.append(div[j][0])
        go_list.append('하고')
    elif div[-1][-1] == 'NNG' and div[-1][0][-1] == '인':
        for j in range(len(div) - 1):
            go_list.append(div[j][0])
        new_in = div[-1][0][:-1] + '이고'
        go_list.append(new_in)
    elif div[-1][-1] == 'JKG' and div[-1][0] == '의':
        for j in range(len(div) - 1):
            go_list.append(div[j][0])
        go_list.append('이고')
    else:
        # print(div)
        pass
    
    if go_list == []:
        return (filter1 + ' 그리고')
    else:
        return_val = ''.join(go_list)
    
    for i in range(len(return_val)):
        if ('ㄱ' in return_val[i]) or ('ㄴ' in return_val[i]) or ('ㄷ' in return_val[i]) or ('ㄹ' in return_val[i]) or ('ㅁ' in return_val[i]) or ('ㅂ' in return_val[i]) or ('ㅅ' in return_val[i]) or ('ㅇ' in return_val[i]) or ('ㅈ' in return_val[i]) or ('ㅊ' in return_val[i]) or ('ㅋ' in return_val[i]) or ('ㅌ' in return_val[i]) or ('ㅍ' in return_val[i]) or ('ㅎ' in return_val[i]):
            return (filter1 + ' 그리고')
    return return_val

def make_df(cl, ncl, cku, ncku, ckuv, nckuv):
    is_it_clear = []
    is_it_not_clear = []
    
    for i in range(len(cl)):
        is_it_clear.append(0)
    
    for i in range(len(ncl)):
        is_it_not_clear.append(1)
    
    clear_df = pd.DataFrame({'sentence' : cl, 'used_keytalk' : cku, 'used_keytalk_verbal' : ckuv, 'is_it_clear' : is_it_clear})
    not_clear_df = pd.DataFrame({'sentence' : ncl, 'used_keytalk' : ncku, 'used_keytalk_verbal' : nckuv, 'is_it_clear' : is_it_not_clear})
    
    merged_df = pd.concat([clear_df, not_clear_df], ignore_index = True)
    
    merged_df.to_excel('형식테스트.xlsx')

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

meta_keytalk_10 = []
filter_keytalk_10 = {}

meta_keytalk_11 = []
filter_keytalk_11 = {}

meta_keytalk_22 = []
filter_keytalk_22 = {}

keytalk_file = pd.read_excel('kakao_keytalk_list_200526_수정_new.xlsx')

for i in range(len(keytalk_file)):
    if '10' in keytalk_file['vertical'][i]:
        if keytalk_file['kl_type'][i] == 'meta':
            meta_keytalk_10.append(keytalk_file['keytalk'][i])
        elif keytalk_file['kl_type'][i] == 'filter':
            filter_keytalk_10[keytalk_file['keytalk'][i]] = keytalk_file['kl_category'][i]
    elif '11' in keytalk_file['vertical'][i]:
        if keytalk_file['kl_type'][i] == 'meta':
            meta_keytalk_11.append(keytalk_file['keytalk'][i])
        elif keytalk_file['kl_type'][i] == 'filter':
            filter_keytalk_11[keytalk_file['keytalk'][i]] = keytalk_file['kl_category'][i]
    elif '22' in keytalk_file['vertical'][i]:
        if keytalk_file['kl_type'][i] == 'meta':
            meta_keytalk_22.append(keytalk_file['keytalk'][i])
        elif keytalk_file['kl_type'][i] == 'filter':
            filter_keytalk_22[keytalk_file['keytalk'][i]] = keytalk_file['kl_category'][i]
    
print('필터 + 메타 + 필터의 조합은 1,')
print('필터 + 필터의 조합은 2를 눌러주세요')

while True:
    user_input = input('입력 : ')
    if user_input == '1' or user_input == '2':
        break
    print('Wrong input')
    

clear_list = []
not_clear_list = []
clear_keytalk_used = []
not_clear_keytalk_used = []
clear_keytalk_used_verbal = []
not_clear_keytalk_used_verbal = []

connection_words = ['이고', '이면서']

while True:
    try:
        repeat_num = input('키토크 분류당 반복할 횟수를 입력해주세요 : ')
        repeat_num = int(repeat_num)
    except:
        print('Wrong input')
    else:
        print()
        break

for i in range(repeat_num):
    if user_input == '1':
        a, b, c = word_concat(meta_keytalk_10, list(filter_keytalk_10.keys()))
        connection = connection_words[random.randint(0, len(connection_words) - 1)]

        expression_loc = ["" for _ in range(2)]

        loc = random.randint(0, 1)
        
        if loc == 0:
            expression_list = get_expression(filter_keytalk_10[a])
        else:
            expression_list = get_expression(filter_keytalk_10[c])
            
        expression = expression_list[random.randint(0, len(expression_list) - 1)]
        expression_loc[loc] = expression + ' '

        if loc == 0:
            tf = get_error(expression, a, (b + connection), c, '웹툰')
        else:
            tf = get_error(a, (b + connection),expression, c, '웹툰')

        if tf == True:
            clear_list.append(expression_loc[0] + a + ' ' + b + connection + ' ' + expression_loc[1] + c + ' 웹툰')
            clear_keytalk_used.append(a + ',' + b + ',' + c)
        else:
            not_clear_list.append(expression_loc[0] + a + ' ' + b + connection + ' ' + expression_loc[1]+  c + ' 웹툰')
            not_clear_keytalk_used.append(a + ',' + b + ',' + c)
    else:
        a, b = word_concat_no_meta(list(filter_keytalk_10.keys()))
        
        expression_list = get_expression(filter_keytalk_10[a])
        expression = expression_list[random.randint(0, len(expression_list) - 1)]
        
        new_a = filter_connection(a)
        
        tf = get_error(expression, new_a, b, '웹툰')
        
        if tf == True:
            clear_list.append(expression + ' ' + new_a + ' ' + b + ' 웹툰')
            clear_keytalk_used.append(a + ',' + b)
        else:
            not_clear_list.append(expression + ' ' + new_a + ' ' + b + ' 웹툰')
            not_clear_keytalk_used.append(a + ',' + b)
    
# print('-------------------------------------------------------------------------------')
    
for i in range(repeat_num):
    if user_input == '1':
        a, b, c = word_concat(meta_keytalk_11, list(filter_keytalk_11.keys()))
        connection = connection_words[random.randint(0, len(connection_words) - 1)]

        expression_loc = ["" for _ in range(2)]

        loc = random.randint(0, 1)
        
        if loc == 0:
            expression_list = get_expression(filter_keytalk_11[a])
        else:
            expression_list = get_expression(filter_keytalk_11[c])

        expression = expression_list[random.randint(0, len(expression_list) - 1)]
        expression_loc[loc] = expression + ' '

        if loc == 0:
            tf = get_error(expression, a, (b + connection), c, '소설')
        else:
            tf = get_error(a, (b + connection),expression, c, '소설')

        if tf == True:
            clear_list.append(expression_loc[0] + a + ' ' + b + connection + ' ' + expression_loc[1] + c + ' 소설')
            clear_keytalk_used.append(a + ',' + b + ',' + c)
        else:
            not_clear_list.append(expression_loc[0] + a + ' ' + b + connection + ' ' + expression_loc[1]+  c + ' 소설')
            not_clear_keytalk_used.append(a + ',' + b + ',' + c)
    else:
        a, b = word_concat_no_meta(list(filter_keytalk_11.keys()))
        
        expression_list = get_expression(filter_keytalk_11[a])
        expression = expression_list[random.randint(0, len(expression_list) - 1)]
        
        new_a = filter_connection(a)
        
        tf = get_error(expression, new_a, b, '소설')
        
        if tf == True:
            clear_list.append(expression + ' ' + new_a + ' ' + b + ' 소설')
            clear_keytalk_used.append(a + ',' + b)
        else:
            not_clear_list.append(expression + ' ' + new_a + ' ' + b + ' 소설')
            not_clear_keytalk_used.append(a + ',' + b)

    
# print('-------------------------------------------------------------------------------')
    
for i in range(repeat_num):
    if user_input == '1':
        a, b, c = word_concat(meta_keytalk_22, list(filter_keytalk_22.keys()))
        connection = connection_words[random.randint(0, len(connection_words) - 1)]

        expression_loc = ["" for _ in range(2)]

        loc = random.randint(0, 1)
        
        if loc == 0:
            expression_list = get_expression(filter_keytalk_22[a])
        else:
            expression_list = get_expression(filter_keytalk_22[c])

        expression = expression_list[random.randint(0, len(expression_list) - 1)]
        expression_loc[loc] = expression + ' '

        if loc == 0:
            tf = get_error(expression, a, (b + connection), c, '방송')
        else:
            tf = get_error(a, (b + connection),expression, c, '방송')

        if tf == True:
            clear_list.append(expression_loc[0] + a + ' ' + b + connection + ' ' + expression_loc[1] + c + ' 방송')
            clear_keytalk_used.append(a + ',' + b + ',' + c)
        else:
            not_clear_list.append(expression_loc[0] + a + ' ' + b + connection + ' ' + expression_loc[1]+  c + ' 방송')
            not_clear_keytalk_used.append(a + ',' + b + ',' + c)
    else:
        a, b = word_concat_no_meta(list(filter_keytalk_22.keys()))
        
        expression_list = get_expression(filter_keytalk_22[a])
        expression = expression_list[random.randint(0, len(expression_list) - 1)]
        
        new_a = filter_connection(a)
        
        tf = get_error(expression, new_a, b, '방송')
        
        if tf == True:
            clear_list.append(expression + ' ' + new_a + ' ' + b + ' 방송')
            clear_keytalk_used.append(a + ',' + b)
        else:
            not_clear_list.append(expression + ' ' + new_a + ' ' + b + ' 방송')
            not_clear_keytalk_used.append(a + ',' + b)
        
# print('-------------------------------------------------------------------------------')

for i in clear_keytalk_used:
    change_list = i.split(',')
    concat_str = []
    for j in change_list:
        j_temp = j
        while True:
            split_text = pro_rules(j_temp)[0]
            change_num = pro_rules(j_temp)[1]
            if change_num == 0:
                strstr1 = j_temp
                break
            # print(split_text)
            strstr1 = ''
            for k in split_text:
                if k[-1] == ' ':
                    k[-1] = None
                try:
                    if len(k) == 1:
                        strstr1 += k[0]
                    else:
                        concat_text = join_jamos_char(k[0], k[1], k[-1])
                        # print(concat_text)
                        strstr1 += concat_text
                except:
                    strstr1 += ' '
            # print(strstr1)
            j_temp = strstr1
        concat_str.append(strstr1)
    # print(concat_str)
    end_str = ''
    for j in concat_str:
        end_str += j
        end_str += ','
    clear_keytalk_used_verbal.append(end_str[:-1])
    
for i in not_clear_keytalk_used:
    change_list = i.split(',')
    concat_str = []
    for j in change_list:
        j_temp = j
        while True:
            split_text = pro_rules(j_temp)[0]
            change_num = pro_rules(j_temp)[1]
            if change_num == 0:
                strstr1 = j_temp
                break
            # print(split_text)
            strstr1 = ''
            for k in split_text:
                if k[-1] == ' ':
                    k[-1] = None
                try:
                    if len(k) == 1:
                        strstr1 += k[0]
                    else:
                        concat_text = join_jamos_char(k[0], k[1], k[-1])
                        # print(concat_text)
                        strstr1 += concat_text
                except:
                    strstr1 += ' '
            # print(strstr1)
            j_temp = strstr1
        concat_str.append(strstr1)
    # print(concat_str)
    end_str = ''
    for j in concat_str:
        end_str += j
        end_str += ','
    not_clear_keytalk_used_verbal.append(end_str[:-1])


# print(clear_keytalk_used_verbal)
# print(not_clear_keytalk_used_verbal)


print('End')

# 데이터프레임으로 보내기
make_df(clear_list, not_clear_list, clear_keytalk_used, not_clear_keytalk_used, clear_keytalk_used_verbal, not_clear_keytalk_used_verbal)






