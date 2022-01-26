# 1.create list of 100 random numbers from 0 to 1000

from random import randint

# Declaring variables
llist = []
ordered_llist = []
even_list = []
odd_list = []

# filling list with random values using randint function
llist = [randint(0, 1000) for i in range(100)]

# section used for debug
# print(llist)
# print('min = ', min(llist))
# print('max = ', max(llist))
# print('sum = ', sum(llist))
# print('lengt llist = '+str(len(llist)))

# 2.sorting list from min to max (without using sort())

# in this step we fill new list with ordered values from min to max.
# llist become clear and for next calculations we should use ordered_llist
for j in range(len(llist)):
    min_k = min(llist)
    ordered_llist.append(min_k)
    llist.remove(min_k)

# section used for debug
# print(ordered_llist)
# print('lengt ordered_llist = '+str(len(ordered_llist)))
# print('sum = ', sum(ordered_llist))

# 3.calculate average for even and odd numbers

# filling even_list and odd_list lists with even and odd values
even_list = [int(i) for i in ordered_llist if i % 2 == 0]
odd_list = [int(i) for i in ordered_llist if i % 2 != 0]

# section used for debug
# print(even_list)
# print('lengt even_list = '+str(len(even_list)))

# section used for debug
# print(odd_list)
# print('lengt odd_list = '+str(len(odd_list)))


# 4.print both average result in console

print('average even numbers = '+str(sum(even_list)/len(even_list)))
print('average odd numbers = '+str(sum(even_list)/len(odd_list)))
