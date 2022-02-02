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


a = [{'j': 27, 'd': 10},
     {'l': 81, 'j': 77, 'p': 100, 'g': 84},
     {'s': 98, 'j': 35, 'c': 63, 'h': 66, 'z': 29, 'u': 62, 'o': 92, 't': 90},
     {'t': 80, 'c': 63},
     {'j': 77}]
keys = []
keys_numbered = []
values = []
final_dict = {}
dict_with_indexes = {}  # key:number_of_dict
dict_with_max_values = {}  # key:max_value
dict_is_has_duplicates = {}  # 0 or 1 in case if there's duplicate, but first value is bigger

for i in a:
    for key, value in i.items():
        if key not in dict_with_max_values or (dict_with_max_values and value > dict_with_max_values.get(key)):
            dict_with_max_values[key] = value

for i in a:
    for key in i.keys():
        if key not in dict_is_has_duplicates:
            dict_is_has_duplicates[key] = 0
        else:
            dict_is_has_duplicates[key] = 1

co = 1
for i in a:
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
