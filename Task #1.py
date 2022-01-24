# create list of 100 random numbers from 0 to 1000
import random

llist = []
ordered_llist = []
even_list = []
odd_list = []

# for i in range(0, 100):
#     l1 = (random.randrange(1, 1000))
#     llist.append(l1)
#     i+1

# better variant
llist = [random.randint(0, 1000) for i in range(100)]

print(llist)
print('min = ', min(llist))
print('max = ', max(llist))
print('sum = ', sum(llist))


print('lengt llist = '+str(len(llist)))

# sort list from min to max (without using sort())

for j in range(len(llist)):
    min_k = min(llist)
    ordered_llist.append(min_k)
    llist.remove(min_k)

print(ordered_llist)
print('lengt ordered_llist = '+str(len(ordered_llist)))
print('sum = ', sum(ordered_llist))

# calculate average for even and odd numbers

even_list = [int(i) for i in ordered_llist if i % 2 == 0]
odd_list = [int(i) for i in ordered_llist if i % 2 != 0]

print(even_list)
print('lengt even_list = '+str(len(even_list)))
print('avg even_list = '+str(sum(even_list)/len(even_list)))

print(odd_list)
print('lengt odd_list = '+str(len(odd_list)))
print('avg odd_list = '+str(sum(even_list)/len(odd_list)))



# print both average result in console