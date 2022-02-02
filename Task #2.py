"""
1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
"""

# import section
import random
import string

# declaring section
dict_list = []
result_dict = {}
common_count_of_dicts = 0
count_of_keys_in_dict = 0

# generating number of dicts
count_of_dicts = random.randint(2, 10)
# print('count_of_dicts:', count_of_dicts)

while common_count_of_dicts < count_of_dicts:
    dict_a = {}
    # generating random length list of unique keys for each dictionary
    count_of_keys_in_dict = random.randint(2, 26)
    # print('count_of_keys_in_dict:', count_of_keys_in_dict)
    keys_list = random.sample(string.ascii_lowercase, count_of_keys_in_dict)
    # print('keys_list:', keys_list)

    # generating dictionaries
    for i in keys_list:
        random_value = random.randint(1, 100)
        # print(random_key, random_value)
        dict_a[i] = random_value

    dict_list.append(dict_a)  # appending dict_list
    common_count_of_dicts = common_count_of_dicts + 1  # rising count by 1
# print(key)
# print(random_key)
# print(random_value)
# print(dict_list)

"""
2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
"""

values = []
final_dict = {}
dict_with_indexes = {}  # key:number_of_dict
dict_with_max_values = {}  # key:max_value
dict_is_has_duplicates = {}  # 0 or 1 in case if there are duplicates, but first value is bigger

for i in dict_list:
    for key, value in i.items():
        if key not in dict_with_max_values or (dict_with_max_values and value > dict_with_max_values.get(key)):
            dict_with_max_values[key] = value

for i in dict_list:
    for key in i.keys():
        if key not in dict_is_has_duplicates:
            dict_is_has_duplicates[key] = 0
        else:
            dict_is_has_duplicates[key] = 1

cnt = 1
for i in dict_list:
    for key, value in i.items():
        if cnt == 1:
            dict_with_indexes[key] = key

        elif cnt != 1 and key not in dict_with_indexes and dict_is_has_duplicates[key] == 0:
            dict_with_indexes[key] = key

        elif cnt != 1 and key not in dict_with_indexes and dict_is_has_duplicates[key] != 0:
            dict_with_indexes[key] = key + '_' + str(cnt)

        elif cnt != 1 and key in dict_with_indexes \
                and value == dict_with_max_values.get(key) \
                and key == dict_with_indexes.get(key):
            dict_with_indexes[key] = key + '_' + str(cnt)
    cnt = cnt + 1

# Print version used for debug
# print('keys and max values:', dict_with_max_values)
# print('keys with duplicates:', dict_is_has_duplicates)
# print('keys with indexes:', dict_with_indexes)
# print('dict_is_has_duplicates:', dict_is_has_duplicates)

# Appending new dictionary key = key with dictionary number in order : value = MAX value for this key in all    /n
# dictionaries and MIN dictionary number in order in case of duplicates

for key, value in dict_with_indexes.items():
    final_dict[value] = dict_with_max_values.get(key)

print('final_dict:', final_dict)
