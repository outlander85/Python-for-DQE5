# 1. create a list of random number of dicts (from 2 to 10)
#
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]


# import section
import random
import string

# declaring section
dict_list = []
result_dict = {}
# keys_list = []
# dict_a = {}

# generating number of dicts
for r in range(2, random.randint(2, 10)):

    # generating random lenght list of unique keys for each dictionary
    # declaring and re-creating for next circle
    keys_list = []
    dict_a = {}

    keys_list = random.sample(string.ascii_lowercase, random.randint(2, 10))

    # appending dictionaries
    for i in keys_list:
        random_key = i
        random_value = random.randint(1, 100)
        # print(random_key, random_value)
        dict_a[random_key] = random_value
        # print(len(keys_list))
        # print(dict_a)

    dict_list.append(dict_a)

# print(key)
# print(random_key)
# print(random_value)
print(dict_list)

# 2. get previously generated list of dicts and create one common dict:
#
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

keys = []
keys_numbered = []
values = []
final_dict = {}
dict_with_indexes = {}  # key:number_of_dict
dict_with_max_values = {}  # key:max_value
dict_is_has_duplicates = {}  # 0 or 1 in case if there's duplicate, but first value is bigger

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

co = 1
for i in dict_list:
    for key, value in i.items():
        if co == 1:
            dict_with_indexes[key] = key

        elif co != 1 and key not in dict_with_indexes and dict_is_has_duplicates[key] == 0:
            dict_with_indexes[key] = key

        elif co != 1 and key not in dict_with_indexes and dict_is_has_duplicates[key] != 0:
            dict_with_indexes[key] = key + '_' + str(co)

        elif co != 1 and key in dict_with_indexes \
                and value == dict_with_max_values.get(key) \
                and key == dict_with_indexes.get(key):
            dict_with_indexes[key] = key + '_' + str(co)
    co = co + 1

# print('keys and max values:', dict_with_max_values)
# print('keys with duplicates:', dict_is_has_duplicates)
# print('keys with indexes:', dict_with_indexes)
# print('dict_is_has_duplicates:', dict_is_has_duplicates)

for key, value in dict_with_indexes.items():
    final_dict[value] = dict_with_max_values.get(key)

print('final_dict:', final_dict)
