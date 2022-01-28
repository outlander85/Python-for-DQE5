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
keys_list = []
dict_a = {}
result_dict = {}

# generating number of dicts
for r in range(2, random.randint(2, 10)):

    # generating random lenght list of unique keys for each dictionary
    keys_list = random.sample(string.ascii_letters, random.randint(2, 10))

    # appending dictionaries
    for i in keys_list:
        random_key = i
        random_value = random.randint(1, 100)
        # print(random_key, random_value)
        dict_a[random_key] = random_value


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
