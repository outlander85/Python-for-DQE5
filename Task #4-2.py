#  From task #2
"""
1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
"""

# import section
from random import randint, sample
import string

# declaring section
result_dict = {}


def rand_numeric(min_element=1, max_element=100):
    return randint(min_element, max_element)


def gen_dict(cod):
    common_count_of_dicts = 0
    dl = []
    while common_count_of_dicts < cod:
        dict_a = {}
        # generating random length list of unique keys for each dictionary
        keys_list = sample(string.ascii_lowercase, rand_numeric(2, 26))
        # generating dictionaries
        for i in keys_list:
            random_value = rand_numeric(1, 100)
            # print(random_key, random_value)
            dict_a[i] = random_value
            # print(random_value)
        dl.append(dict_a)  # appending dict_list
        common_count_of_dicts += 1  # rising count by 1
    return dl


def dict_with_max_values_f(dl):  # Dictionary list
    dmv = {}
    for i in dl:
        for key, value in i.items():
            if key not in dmv or (dmv and value > dmv.get(key)):
                dmv[key] = value
    return dmv


def dict_is_has_duplicates_f(dl):  # Dictionary list
    dhd = {}
    for i in dl:
        for key in i.keys():
            if key not in dhd:
                dhd[key] = 0
            else:
                dhd[key] = 1
    return dhd


# generating number of dicts
count_of_dicts = rand_numeric(2, 10)
dict_list = gen_dict(count_of_dicts)
# print(dict_list)


def dict_with_indexes_f(dhd, dmv):
    dwi = {}  # key:number_of_dict
    cnt = 1
    for i in dict_list:
        for key, value in i.items():
            if cnt == 1:
                dwi[key] = key

            elif cnt != 1 and key not in dwi and dict_is_has_duplicates[key] == 0:
                dwi[key] = key

            elif cnt != 1 and key not in dwi and dict_is_has_duplicates[key] != 0:
                dwi[key] = key + '_' + str(cnt)

            elif cnt != 1 and key in dwi \
                    and value == dict_with_max_values.get(key) \
                    and key == dwi.get(key):
                dwi[key] = key + '_' + str(cnt)
        cnt = cnt + 1
    return dwi


"""
2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
"""

values = []
final_dict = {}

dict_with_max_values = dict_with_max_values_f(dict_list)  # key:max_value
dict_is_has_duplicates = dict_is_has_duplicates_f(dict_list)  # 0 or 1 in case if there are duplicates, first is bigger
dict_with_indexes = dict_with_indexes_f(dict_is_has_duplicates, dict_with_max_values)

# Print version used for debug
# print('dict_list:', dict_list)
# print('keys and max values:', dict_with_max_values)
# print('keys with duplicates:', dict_is_has_duplicates)
# print('keys with indexes:', dict_with_indexes)

# Appending new dictionary key = key with dictionary number in order : value = MAX value for this key in all    /n
# dictionaries and MIN dictionary number in order in case of duplicates

for key, value in dict_with_indexes.items():
    final_dict[value] = dict_with_max_values.get(key)

print('final_dict:', final_dict)
