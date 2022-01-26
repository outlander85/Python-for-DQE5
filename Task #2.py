# 1. create a list of random number of dicts (from 2 to 10)
#
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]


# import section
import random
import string
import collections

dict_list = []
dict_a = {}
result_dict = {}
for r in range(2, random.randint(2, 10)):

    for i in range(2, random.randint(2, 10)):
        key = string.ascii_letters
        random_key = random.choice(key)
        random_value = random.randint(1, 100)
        # print(random_key, random_value)
        dict_a[random_key] = random_value
        i+1

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
