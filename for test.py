# def create_random_str(str_len: int = 20, upper_case: bool = False, lower_case: bool = True, digits: bool = False):
#     condition = ''
#     if upper_case:
#         condition = condition + string.ascii_uppercase
#     if lower_case:
#         condition = condition + string.ascii_lowercase
#     if digits:
#         condition = condition + string.digits
#     return ''.join(random.choices(condition, k=str_len))


# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")
#
#
# a = [{'j': 27, 'd': 10},
#      {'l': 81, 'j': 77, 'p': 100, 'g': 84},
#      {'s': 98, 'j': 35, 'c': 63, 'h': 66, 'z': 29, 'u': 62, 'o': 92, 't': 90},
#      {'t': 80, 'c': 63},
#      {'j': 77}]
# keys = []
# keys_numbered = []
# values = []
# final_dict = {}
# dict_with_indexes = {}  # key:number_of_dict
# dict_with_max_values = {}  # key:max_value
# dict_is_has_duplicates = {}  # 0 or 1 in case if there's duplicate, but first value is bigger
#
# for i in a:
#     for key, value in i.items():
#         if key not in dict_with_max_values or (dict_with_max_values and value > dict_with_max_values.get(key)):
#             dict_with_max_values[key] = value
#
# for i in a:
#     for key in i.keys():
#         if key not in dict_is_has_duplicates:
#             dict_is_has_duplicates[key] = 0
#         else:
#             dict_is_has_duplicates[key] = 1
#
# co = 1
# for i in a:
#     for key, value in i.items():
#         if co == 1:
#             dict_with_indexes[key] = key
#
#         elif co != 1 and key not in dict_with_indexes and dict_is_has_duplicates[key] == 0:
#             dict_with_indexes[key] = key
#
#         elif co != 1 and key not in dict_with_indexes and dict_is_has_duplicates[key] != 0:
#             dict_with_indexes[key] = key + '_' + str(co)
#
#         elif co != 1 and key in dict_with_indexes \
#                 and value == dict_with_max_values.get(key) \
#                 and key == dict_with_indexes.get(key):
#             dict_with_indexes[key] = key + '_' + str(co)
#     co = co + 1
#
# # print('keys and max values:', dict_with_max_values)
# # print('keys with duplicates:', dict_is_has_duplicates)
# # print('keys with indexes:', dict_with_indexes)
# # print('dict_is_has_duplicates:', dict_is_has_duplicates)
#
# for key, value in dict_with_indexes.items():
#     final_dict[value] = dict_with_max_values.get(key)
#
# print('final_dict:', final_dict)

# k = 1
# for i in a:
#     for key, value in i.items():
#         if k == 1:
#             dict_with_indexes[key] = key
#         else:
#             dict_with_indexes[key] = key + '_' + str(k)
#     k = k + 1
# print(dict_with_indexes)


#
#
# for i in a:
#
#     for key, value in i.items():
#
#         if k == 1:
#             key_v = key
#         else:
#             if key in keys:
#                 key_v = key + '_' + str(k)
#             else:
#                 key_v = key
#         val_v = value
#         keys.append(key_v)
#         values.append(value)
#
#     k = k + 1
# # print(keys, values)
#
# keys_and_values = dict(zip(keys, values))
# print(keys_and_values)

# for key, value in keys_and_values.items():
#     if
"""
a1 = ['a', 'b', 'c', 'a', 'a', 'b']
a2 = []

d = {}

for i in a1:

    d.setdefault(i, 0)
    d[i] += 1

    if d[i] >= 2:
        a2.append('%s_%d' % (i, d[i]))
    else:
        a2.append(i)

print(a2)
"""

# a = """text
# """
# print(len(a))
# print(a[4])

# txt = "welcome to the jungle"
#
# x = txt.split()
#
# print(x)

# print(" iZ ".lower())
#
# variable = """homEwork:
# 	tHis iz your homeWork, copy these Text to variable.
#
# 	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
#
# 	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
#
# 	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
#
# variable = ' '.join([s[0].upper() + s[1:] for s in variable.split('/n')])
#
# print(variable)


# s = 'a;b;c;d'
# slist = list(s)
# for i, c in enumerate(slist):
#     if slist[i] == ';' and 0 <= i <= 3: # only replaces semicolons in the first part of the text
#         slist[i] = ':'
# s = ''.join(slist)
# print(s) # prints a:b:c;d
# usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# for i in range(len(usernames)):
#     usernames[i] = usernames[i].lower().replace(" ", "_")
#
# print(usernames)

import re

a5 = """Homework:
	This is your homework, copy these text to variable.
	You need to normalize it from letter cases point of view. also, create one more sentence with last words of each existing sentence and add it to the end of this paragraph.
	It is misspelling here. fix “iz” with correct “is”, but only when it is a mistake.
	Last is to calculate number of whitespace characters in this text. carefull, not only spaces, but all whitespaces. i got 87. 
	Variable view paragraph here mistake text whitespaces 87."""

# print('a5:', a5, '\n')
# print('a5:', repr(a5), '\n')
#
# a101 = a5.split('.')
#
# for a in a101:
#     for i in a:
#         if i[0] == ' ':
#             b[0] == ''
#
#         else:
#             b = i
#         print(b)


#
# a100 = a5.split(':')
# for i, j in enumerate(a100):
#     if '.' in a100[:i] and a100[i].isalpha():
#         c = a100[:i] + a100[i].lower() + a100[i+1:]
#         a100 = c
#         break
# print(a100)



    # print(i, repr(j))
# print(a100)

# result = re.sub(r'\. \w', '1', a5)
# print(result)


from pydoc import replace
import re


# raw_string = '''homEwork:
#    tHis iz your homeWork, copy these Text to variable.
#    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
#    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
#    last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
# '''

choose = ''
print('Please choose publication variant:\n1 - for %s\n2 - for %s\n3 - for %s' %
      ('NEWS', 'ADVERTISEMENT', 'PROMOCODE'))
try:
    choose = int(input())
except ValueError:
    print("You've entered wrong value")

mode = ''

if choose == 1:
    mode = 'NEWS'
elif choose == 2:
    mode = 'ADVERTISEMENT'
elif choose == 3:
    mode = 'PROMOCODE'
else:
    # print('Please make correct choice')
    mode = None

if choose in (1, 2, 3):
    print(f"You've chosen {mode}")
else:
    print('Please make correct choice')
