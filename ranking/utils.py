from collections import Iterable
import re


def flatten(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flatten(item):
                yield x
        else:
            yield item


def returnNum(current_answer, comp_type):
    numbers = []
    if comp_type == 'more_than' or comp_type == 'less_than':
        word_list = [num.strip() for num in current_answer.split('than')]
    elif comp_type == 'to':
        word_list = [num.strip() for num in current_answer.split('to')]
    for word in word_list:
        alnums = re.findall("\d", word)
        if word.isnumeric():
            if float(word) not in numbers:
                numbers.append(int(float(word)))
        elif alnums:
            word_list1 = [num.strip() for num in current_answer.split(' ')]
            for word1 in word_list1:
                if word1.isnumeric():
                    if float(word1) not in numbers:
                        numbers.append(int(float(word1)))
                elif '0.' in word1:
                    if float(word1) not in numbers:
                        numbers.append((float(word1)))
    return numbers


def returnRiskType(risk_score):
    if risk_score < 30:
        risk_type = 'Least Vulnerable'
    elif risk_score >= 30 and risk_score <= 70:
        risk_type = 'Medium Vulnerable'
    elif risk_score > 70:
        risk_type = 'Highly Vulnerable'
    else:
        risk_type = 'Medium Vulnerable'
    return risk_type


'''
This function returns a integer or a float and string from a string given
'''
def splitIntStr(string):
    if string.strip().isalnum():
        if string.strip().isalpha():
            this_num = 0
            this_string = string
        else:
            values = [s for s in string if not s.isalpha()]
            value_str = ''
            for st in values:
                value_str = value_str + st
            this_num = float(value_str)
            values = [s for s in string if s.isalpha()]
            this_string = ''
            for st in values:
                this_string = this_string + st
    elif '.' in string.strip():
        if ' ' in string.strip():
            striped_string = [s for s in string.split(" ") if s != '']
            for st in striped_string:
                if st.isnumeric():
                    this_num = float(st)
                elif st.replace('.', '', 1).isdigit():
                    this_num = float(st)
                elif st.isalpha():
                    this_string = st
                else:
                    this_num = 0
                    this_string = st
        else:
            all_chars = [s for s in string]
            this_num = ''.join(e for e in all_chars if not str(e).isalpha())
            this_num = float(this_num)
            this_string = ''.join(str(e)
                                  for e in all_chars if str(e).isalpha())
    elif ' ' in string.strip():
        striped_string = [s for s in string.split(" ") if s != '']
        for st in striped_string:
            if st.isnumeric():
                this_num = float(st)
            elif st.isalpha():
                this_string = st
    elif '-' in string.strip():
        all_chars = [s for s in string]
        striped_str = ''.join(e for e in all_chars if not str(e).isalpha())
        num_list = [s for s in striped_str.split("-") if s != '']
        num1 = float(num_list[0])
        num2 = float(num_list[1])
        this_num = num1 + num2
        this_string = ''.join(str(e) for e in all_chars if str(e).isalpha())
    else:
        this_num = float(string)
        this_string = ''
    return [this_num, this_string]
