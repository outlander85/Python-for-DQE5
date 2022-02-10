import string
import re
from pydoc import replace

variable = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""



def lower_f(var):
    var = var.lower()
    return var


def split_f(str_row='', delimeter="\n"):
    str_row = str_row.split(delimeter)
    return str_row


def delete_ns_f(str_row='', delimeter="\n"):
    a = 0
    a2 = split_f(str_row, delimeter)
    while a < len(a2):
        if a2[a] == '' or a2[a] == ' ':
            a2.remove(a2[a])
        else:
            a = a + 1
    return a2


def additional_sentence_f(str_row=''):
    additional_sentence_words = []
    a6 = str_row.split()

    for i in range(len(a6)):
        if re.findall('[.!?]', a6[i]):
            additional_sentence_words.append(re.sub('[.!?]', '', a6[i]))
    additional_sentence = ' '.join(additional_sentence_words).capitalize()
    return additional_sentence


def final_sentence_f(str_row, add_sentence):
    final_sentence = []
    a7 = str_row.split('.')
    while a7:
        a8 = a7.pop(0)
        counter = 0
        for i in a8:
            if not i.isalpha():
                counter += 1
            elif i == ' ':
                replace(a8, '')
            else:
                break
        a8 = a8[:counter] + a8[counter:].capitalize()
        if 'this paragraph' in a8:
            a8 = a8 + '. ' + add_sentence
        final_sentence.append(a8)
    final_sentence = '.'.join(final_sentence)
    return final_sentence


def count_of_whitespaces(str_row):
    cnt = 0
    for i in range(0, len(str_row)):
        if str_row[i] in string.whitespace:
            cnt += 1
    return cnt


variable = lower_f(variable)
# print('variable:', repr(variable))

a2 = delete_ns_f(variable, "\n")
# print('a2:', a2)

a3 = [x.strip() for x in a2]
# print('a3:', a3)

a4 = "\n\t".join(a3)
# print('a4:', a4)
# print('a4:', repr(a4))

a5 = a4.replace('“iz”', ' “iz”').replace(' iz ', ' is ')
# print('a5:', a5)

additional_sentence = additional_sentence_f(a5)
# print(additional_sentence)

final_sentence = final_sentence_f(a5, additional_sentence)

cnt = count_of_whitespaces(final_sentence)

print(final_sentence)
print('\nNumber of whitespaces is:', cnt)
