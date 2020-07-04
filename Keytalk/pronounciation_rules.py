#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:45:26 2020

@author: 윤도원
"""
from unicode import korean_split

def pro_rules(text):
    text_split = korean_split(text)
    
    changer_count = 0
    
    # '넓-'은 '넓죽하다', '넓둥글다'일때 '넙'으로 발음한다.
    if text == '넓죽하다':
        changer_count += 1
        return '넙쭈카다', changer_count
    elif text == '넓둥글다':
        changer_count += 1
        return '넙뚱글다', changer_count
    else:
        for i in range(len(text_split)):
            try:
                # 5-3. 자음을 첫소리로 가지고 있는 음절의 ㅢ는 ㅣ로 발음한다.
                if text_split[i][0] != 'ㅇ' and text_split[i][1] == 'ㅢ':
                    text_split[i][1] = 'ㅣ'
                    # print('5-3 occured')
                    changer_count += 1
                    
                # 17. 받침 'ㄷ, ㅌ(ㄾ)'이 조사나 접미사의 모음 'ㅣ'와 결합되는 경우에는, [ㅈ, ㅊ]으로 바꾸어서 뒤 음절 첫소리로 옮겨 발음한다.
                if text_split[i][2] == 'ㄷ' and text_split[i + 1][0] == 'ㅇ' and text_split[i + 1][1] == 'ㅣ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㅈ'
                    # print('17 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅌ' and text_split[i + 1][0] == 'ㅇ' and text_split[i + 1][1] == 'ㅣ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㅊ'
                    # print('17 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄾ' and text_split[i + 1][0] == 'ㅇ' and text_split[i + 1][1] == 'ㅣ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅊ'
                    # print('17 occured')
                    changer_count += 1
                
                # 17-붙임. 'ㄷ' 뒤에 접미사 '히'가 결합되어 '티'를 이루는 것은 [치]로 발음한다.
                if text_split[i][2] == 'ㄷ' and text_split[i + 1][0] == 'ㅎ' and text_split[i + 1][1] == 'ㅣ' and text_split[i + 1][2] == ' ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㅊ'
                    # print('17-붙임 occured')
                    changer_count += 1

                # 12-1. 'ㅎ(ㄶ, ㅀ)' 뒤에 'ㄱ, ㄷ, ㅈ'이 결합되는 경우에는, 뒤 음절 첫소리와 합쳐서 [ㅋ, ㅌ, ㅊ]으로 발음한다.
                if text_split[i][2] == 'ㅎ' and text_split[i + 1][0] == 'ㄱ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㅋ'
                    # print('12-1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅎ' and text_split[i + 1][0] == 'ㄷ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㅌ'
                    # print('12-1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅎ' and text_split[i + 1][0] == 'ㅈ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㅊ'
                    # print('12-1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄶ' and text_split[i + 1][0] == 'ㄱ':
                    text_split[i][2] = 'ㄴ'
                    text_split[i + 1][0] = 'ㅋ'
                    # print('12-1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄶ' and text_split[i + 1][0] == 'ㄷ':
                    text_split[i][2] = 'ㄴ'
                    text_split[i + 1][0] = 'ㅌ'
                    # print('12-1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄶ' and text_split[i + 1][0] == 'ㅈ':
                    text_split[i][2] = 'ㄴ'
                    text_split[i + 1][0] = 'ㅊ'
                    # print('12-1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅀ' and text_split[i + 1][0] == 'ㄱ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅋ'
                    # print('12-1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅀ' and text_split[i + 1][0] == 'ㄷ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅌ'
                    # print('12-1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅀ' and text_split[i + 1][0] == 'ㅈ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅊ'
                    # print('12-1 occured')
                    changer_count += 1

                # 12-1-붙임1. 받침 'ㄱ(ㄺ), ㄷ, ㅂ(ㄼ), ㅈ(ㄵ)'이 뒤 음절 첫소리 'ㅎ'과 결합되는 경우에도, 역시 두 소리를 합쳐서 [ㅋ, ㅌ, ㅍ, ㅊ]으로 발음한다.
                if text_split[i][2] == 'ㄱ' and text_split[i + 1][0] == 'ㅎ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㅋ'
                    # print('12-1-붙임1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄺ' and text_split[i + 1][0] == 'ㅎ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅋ'
                    # print('12-1-붙임1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄷ' and text_split[i + 1][0] == 'ㅎ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㅌ'
                    # print('12-1-붙임1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅂ' and text_split[i + 1][0] == 'ㅎ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㅍ'
                    # print('12-1-붙임1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄼ' and text_split[i + 1][0] == 'ㅎ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅍ'
                    # print('12-1-붙임1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅈ' and text_split[i + 1][0] == 'ㅎ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㅊ'
                    # print('12-1-붙임1 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄵ' and text_split[i + 1][0] == 'ㅎ':
                    text_split[i][2] = 'ㄴ'
                    text_split[i + 1][0] = 'ㅊ'
                    # print('12-1-붙임1 occured')
                    changer_count += 1

                # 12-2. 'ㅎ(ㄶ, ㅀ)' 뒤에 'ㅅ'이 결합되는 경우에는, 'ㅅ'을 [ㅆ]으로 발음한다.
                if text_split[i][2] == 'ㅎ' and text_split[i + 1][0] == 'ㅅ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㅆ'
                    # print('12-2 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄶ' and text_split[i + 1][0] == 'ㅅ':
                    text_split[i][2] = 'ㄴ'
                    text_split[i + 1][0] = 'ㅆ'
                    # print('12-2 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅀ' and text_split[i + 1][0] == 'ㅅ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅆ'
                    # print('12-2 occured')
                    changer_count += 1

                # 12-3. 'ㅎ' 뒤에 'ㄴ'이 결합되는 경우에는, [ㄴ]으로 발음한다.
                if text_split[i][2] == 'ㅎ' and text_split[i + 1][0] == 'ㄴ':
                    text_split[i][2] = 'ㄴ'
                    # print('12-3 occured')
                    changer_count += 1

                # 12-3-붙임. 'ㄶ, ㅀ' 뒤에 'ㄴ'이 결합되는 경우에는, 'ㅎ'을 발음하지 않는다.
                if text_split[i][2] == 'ㄶ' and text_split[i + 1][0] == 'ㄴ':
                    text_split[i][2] = 'ㄴ'
                    # print('12-3-붙임 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅀ' and text_split[i + 1][0] == 'ㄴ':
                    text_split[i][2] = 'ㄹ'
                    # print('12-3-붙임 occured')
                    changer_count += 1

                # 12-4. 'ㅎ(ㄶ, ㅀ)' 뒤에 모음으로 시작된 어미나 접미사가 결합되는 경우에는, 'ㅎ'을 발음하지 않는다.
                if text_split[i][2] == 'ㅎ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = ' '
                    # print('12-4 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄶ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㄴ'
                    # print('12-4 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅀ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = ' '
                    text_split[i + 1][0] = 'ㄹ'
                    # print('12-4 occured')
                    changer_count += 1

                # 13. 홑받침이나 쌍받침이 모음으로 시작된 조사나 어미, 접미사와 결합되는 경우에는, 제 음가대로 뒤 음절 첫소리로 옮겨 발음한다.
                if text_split[i][2] in ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㄲ', 'ㄸ', 'ㅃ', 'ㅆ'] and text_split[i + 1][0] == 'ㅇ':
                    text_split[i + 1][0] = text_split[i][2]
                    text_split[i][2] = ' '
                    # print('13 occured')
                    changer_count += 1

                # 18. 받침 'ㄱ(ㄲ, ㅋ, ㄳ, ㄺ), ㄷ(ㅅ, ㅆ, ㅈ, ㅊ, ㅌ, ㅎ), ㅂ(ㅍ, ㄼ, ㄿ, ㅄ)'은 'ㄴ, ㅁ' 앞에서 [ㅇ, ㄴ, ㅁ]으로 발음한다.
                if text_split[i][2] in ['ㄱ', 'ㄲ', 'ㅋ', 'ㄳ', 'ㄺ'] and text_split[i + 1][0] in ['ㄴ', 'ㅁ']:
                    text_split[i][2] = 'ㅇ'
                    # print('18 occured')
                    changer_count += 1
                if text_split[i][2] in ['ㄷ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ', 'ㅎ'] and text_split[i + 1][0] in ['ㄴ', 'ㅁ']:
                    text_split[i][2] = 'ㄴ'
                    # print('18 occured')
                    changer_count += 1
                if text_split[i][2] in ['ㅂ', 'ㅍ', 'ㄼ', 'ㄿ', 'ㅄ'] and text_split[i + 1][0] in ['ㄴ', 'ㅁ']:
                    text_split[i][2] = 'ㅁ'
                    # print('18 occured')
                    changer_count += 1

                # 19. 받침 'ㅁ, ㅇ' 뒤에 연결되는 'ㄹ'은 [ㄴ]으로 발음한다.
                if text_split[i][2] in ['ㅁ', 'ㅇ'] and text_split[i + 1][0] == 'ㄹ':
                    text_split[i + 1][0] = 'ㄴ'
                    # print('19 occured')
                    changer_count += 1

                # 19-붙임. 받침 'ㄱ, ㅂ' 뒤에 연결되는 'ㄹ'도 [ㄴ]으로 발음한다.
                if text_split[i][2] in ['ㄱ', 'ㅂ'] and text_split[i + 1][0] == 'ㄹ':
                    text_split[i + 1][0] = 'ㄴ'
                    # print('19-붙임 occured')
                    changer_count += 1

                # 20. 'ㄴ'은 'ㄹ'의 앞이나 뒤에서 [ㄹ]로 발음한다.
                if text_split[i][2] == 'ㄴ' and text_split[i + 1][0] == 'ㄹ':
                    text_split[i][2] = 'ㄹ'
                    # print('20 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄹ' and text_split[i + 1][0] == 'ㄴ':
                    text_split[i + 1][0] = 'ㄹ'
                    # print('20 occured')
                    changer_count += 1

                # 20-붙임. 첫소리 'ㄴ'이 'ㅀ, ㄾ' 뒤에 연결되는 경우에도 이에 준한다.
                if text_split[i][2] in ['ㅀ', 'ㄾ'] and text_split[i + 1][0] == 'ㄴ':
                    text_split[i][2] = 'ㄹ'
                    # print('20-붙임 occured')
                    changer_count += 1

                # 23. 받침 'ㄱ(ㄲ, ㅋ, ㄳ, ㄺ), ㄷ(ㅅ, ㅆ, ㅈ, ㅊ, ㅌ), ㅂ(ㅍ, ㄼ, ㄿ, ㅄ)' 뒤에 연결되는 'ㄱ, ㄷ, ㅂ, ㅅ, ㅈ'은 된소리로 발음한다.
                if text_split[i][2] in ['ㄱ', 'ㄲ', 'ㅋ', 'ㄳ', 'ㄺ', 'ㄷ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ', 'ㅂ', 'ㅍ', 'ㄼ', 'ㄿ', 'ㅄ'] and text_split[i + 1][0] == 'ㄱ':
                    text_split[i + 1][0] = 'ㄲ'
                    # print('23 occured')
                    changer_count += 1
                if text_split[i][2] in ['ㄱ', 'ㄲ', 'ㅋ', 'ㄳ', 'ㄺ', 'ㄷ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ', 'ㅂ', 'ㅍ', 'ㄼ', 'ㄿ', 'ㅄ'] and text_split[i + 1][0] == 'ㄷ':
                    text_split[i + 1][0] = 'ㄸ'
                    # print('23 occured')
                    changer_count += 1
                if text_split[i][2] in ['ㄱ', 'ㄲ', 'ㅋ', 'ㄳ', 'ㄺ', 'ㄷ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ', 'ㅂ', 'ㅍ', 'ㄼ', 'ㄿ', 'ㅄ'] and text_split[i + 1][0] == 'ㅂ':
                    text_split[i + 1][0] = 'ㅃ'
                    # print('23 occured')
                    changer_count += 1
                if text_split[i][2] in ['ㄱ', 'ㄲ', 'ㅋ', 'ㄳ', 'ㄺ', 'ㄷ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ', 'ㅂ', 'ㅍ', 'ㄼ', 'ㄿ', 'ㅄ'] and text_split[i + 1][0] == 'ㅅ':
                    text_split[i + 1][0] = 'ㅆ'
                    # print('23 occured')
                    changer_count += 1
                if text_split[i][2] in ['ㄱ', 'ㄲ', 'ㅋ', 'ㄳ', 'ㄺ', 'ㄷ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ', 'ㅂ', 'ㅍ', 'ㄼ', 'ㄿ', 'ㅄ'] and text_split[i + 1][0] == 'ㅈ':
                    text_split[i + 1][0] = 'ㅉ'
                    # print('23 occured')
                    changer_count += 1

                # 24. 어간 받침 'ㄴ(ㄵ), ㅁ(ㄻ)' 뒤에 결합되는 어미의 첫소리 'ㄱ, ㄷ, ㅅ, ㅈ'은 된소리로 발음한다.
                # 다만, 피동, 사동의 접미사 '-기-'는 된소리로 발음하지 않는다.
                # -------------------------------------------------------------------------------이거 대부분의 경우에서 이상하게 나오니까 뺌
#                 if text_split[i][2] in ['ㄴ', 'ㄵ', 'ㅁ', 'ㄻ'] and text_split[i + 1][0] == 'ㄱ' and not(text_split[i + 1][1] == 'ㅣ' and text_split[i + 1][2] == ' '):
#                     text_split[i + 1][0] = 'ㄲ'
#                     print('24 occured')
#                     changer_count += 1
#                 if text_split[i][2] in ['ㄴ', 'ㄵ', 'ㅁ', 'ㄻ'] and text_split[i + 1][0] == 'ㄷ':
#                     text_split[i + 1][0] = 'ㄸ'
#                     print('24 occured')
#                     changer_count += 1
#                 if text_split[i][2] in ['ㄴ', 'ㄵ', 'ㅁ', 'ㄻ'] and text_split[i + 1][0] == 'ㅅ':
#                     text_split[i + 1][0] = 'ㅆ'
#                     print('24 occured')
#                     changer_count += 1
#                 if text_split[i][2] in ['ㄴ', 'ㄵ', 'ㅁ', 'ㄻ'] and text_split[i + 1][0] == 'ㅈ':
#                     text_split[i + 1][0] = 'ㅉ'
#                     print('24 occured')
#                     changer_count += 1

                # 25. 어간 받침 'ㄼ, ㄾ' 뒤에 결합되는 어미의 첫소리 'ㄱ, ㄷ, ㅅ, ㅈ'은 된소리로 발음한다.
                if text_split[i][2] in ['ㄼ', 'ㄾ'] and text_split[i + 1][0] == 'ㄱ':
                    text_split[i + 1][0] = 'ㄲ'
                    # print('25 occured')
                    changer_count += 1
                if text_split[i][2] in ['ㄼ', 'ㄾ'] and text_split[i + 1][0] == 'ㄷ':
                    text_split[i + 1][0] = 'ㄸ'
                    # print('25 occured')
                    changer_count += 1
                if text_split[i][2] in ['ㄼ', 'ㄾ'] and text_split[i + 1][0] == 'ㅅ':
                    text_split[i + 1][0] = 'ㅆ'
                    # print('25 occured')
                    changer_count += 1
                if text_split[i][2] in ['ㄼ', 'ㄾ'] and text_split[i + 1][0] == 'ㅈ':
                    text_split[i + 1][0] = 'ㅉ'
                    # print('25 occured')
                    changer_count += 1

                # 26. 한자어에서, 'ㄹ' 받침 뒤에 연결되는 'ㄷ, ㅅ, ㅈ'은 된소리로 발음한다.
                # 다만, 같은 한자가 겹쳐진 단어의 경우에는 된소리로 발음하지 않는다.
                # --------------------------------------------------------------- 한자어 구분 못하니까 패스

                # 27. 관형사형 '-[으]ㄹ' 뒤에 연결되는 'ㄱ, ㄷ, ㅂ, ㅅ, ㅈ'은 된소리로 발음한다.
                # 다만, 끊어서 말할 적에는 예사소리로 발음한다.
                # --------------------------------------------------------------- 관형사형 구분 못하니까 패스

                # 28. 표기상으로는 사이시옷이 없더라도, 관형격 기능을 지니는 사이시옷이 있어야 할(휴지가 성립되는) 합성어의 경우에는, 뒤 단어의 첫소리 'ㄱ, ㄷ, ㅂ, ㅅ, ㅈ'을 된소리로 발음한다.
                # --------------------------------------------------------------- 처리못함

                # 14. 겹받침이 모음으로 시작된 조사나 어미, 접미사와 결합되는 경우에는, 뒤엣것만을 뒤 음절 첫소리로 옮겨 발음한다. (이 경우, 'ㅅ'은 된소리로 발음함.)
                if text_split[i][2] == 'ㄳ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = 'ㄱ'
                    text_split[i + 1][0] = 'ㅆ'
                    # print('14 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄵ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = 'ㄴ'
                    text_split[i + 1][0] = 'ㅈ'
                    # print('14 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄶ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = 'ㄴ'
                    text_split[i + 1][0] = 'ㅎ'
                    # print('14 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄺ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㄱ'
                    # print('14 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄻ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅁ'
                    # print('14 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄼ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅂ'
                    # print('14 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄽ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅆ'
                    # print('14 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄾ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅌ'
                    # print('14 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄿ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅍ'
                    # print('14 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅀ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = 'ㄹ'
                    text_split[i + 1][0] = 'ㅎ'
                    # print('14 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅄ' and text_split[i + 1][0] == 'ㅇ':
                    text_split[i][2] = 'ㅂ'
                    text_split[i + 1][0] = 'ㅆ'
                    # print('14 occured')
                    changer_count += 1
            except:
                pass
            
            try:
                # 9. 받침 'ㄲ, ㅋ' / 'ㅅ, ㅆ, ㅈ, ㅊ, ㅌ' / 'ㅍ'은 어말 또는 자음 앞에서 각각 대표음 [ㄱ, ㄷ, ㅂ]으로 발음한다.  
                if text_split[i][2] in ['ㄲ', 'ㅋ']:
                    text_split[i][2] = 'ㄱ'
                    # print('9 occured')
                    changer_count += 1
                if text_split[i][2] in ['ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ']:
                    text_split[i][2] = 'ㄷ'
                    # print('9 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅍ':
                    text_split[i][2] = 'ㅂ'
                    # print('9 occured')
                    changer_count += 1
            except:
                pass
            
            try:
                # 10. 겹받침 'ㄳ' / 'ㄵ' / 'ㄼ, ㄽ, ㄾ' / 'ㅄ'은 어말 또는 자음 앞에서 각각 [ㄱ, ㄴ, ㄹ, ㅂ]으로 발음한다.
                # 다만, '밟-'은 자음 앞에서 '밥'으로 발음한다.
                if text_split[i][2] == 'ㄳ':
                    text_split[i][2] = 'ㄱ'
                    # print('10 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄵ':
                    text_split[i][2] = 'ㄴ'
                    # print('10 occured')
                    changer_count += 1
            except:
                pass
            
            try:
                if text_split[i][0] == 'ㅂ' and text_split[i][1] == 'ㅏ' and text_split[i][2] == 'ㄼ' and text_split[i + 1][0] != 'ㅇ':
                    text_split[i][2] = 'ㅂ'
                    # print('10 occured')
                    changer_count += 1
            except:
                pass
            
            try:
                if text_split[i][2] in ['ㄼ', 'ㄽ', 'ㄾ']:
                    text_split[i][2] = 'ㄹ'
                    # print('10 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅄ':
                    text_split[i][2] = 'ㅂ'
                    # print('10 occured')
                    changer_count += 1

                # 11. 겹받침 'ㄺ, ㄻ, ㄿ'은 어말 또는 자음 앞에서 각각 [ㄱ, ㅁ, ㅂ]으로 발음한다.
                # 다만, 용언의 어간 말음 'ㄺ'은 'ㄱ' 앞에서 [ㄹ]로 발음한다.
                # ---------------------------------------------------------------------- 'ㄺ'은 용언처리 불가능하지만 일단 ㄱ으로 바꿔봄
                if text_split[i][2] == 'ㄺ':
                    text_split[i][2] = 'ㄱ'
                    # print('11 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄻ':
                    text_split[i][2] = 'ㅁ'
                    # print('11 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㄿ':
                    text_split[i][2] = 'ㅂ'
                    # print('11 occured')
                    changer_count += 1
            except: 
                pass
            
            try:
                # 최종 음절 끝소리 규칙
                if text_split[i][2] in ['ㄲ', 'ㅋ']:
                    text_split[i][2] = 'ㄱ'
                    # print('음절 끝소리 규칙 occured')
                    changer_count += 1
                if text_split[i][2] in ['ㅌ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅎ']:
                    text_split[i][2] = 'ㄷ'
                    # print('음절 끝소리 규칙 occured')
                    changer_count += 1
                if text_split[i][2] == 'ㅍ':
                    text_split[i][2] = 'ㅂ'
                    # print('음절 끝소리 규칙 occured')
                    changer_count += 1
            except:
                pass
            
    return text_split, changer_count
    