variable = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

import string
import re
a = 0
variable = variable.lower()
print('variable:', repr(variable))

# Delete multi-\n's
a2 = variable.split("\n")
print('a2:', a2)
while a < len(a2):
    if a2[a] == '' or a2[a] == ' ':
        a2.remove(a2[a])
    else:
        a = a+1
print('Modified a2:', a2)

a3 = [x.strip().capitalize() for x in a2]
print('a3:', a3)

a4 = "\n\t".join(a3)
print('a4:', a4)
print('a4:', repr(a4))

a5 = a4.replace('“iz”', ' “iz”').replace(' iz ', ' is ')
print('a5:', a5)
    #     ttr = c.replace(a4[p+2], c[p+2].upper())
    # else:
    #     ttr = a4[p]
    # print(ttr)
# print('CAP:', a4)
# b = 0
# d = 0
# while b < len(a4):
#     if a4(d-2)[b - 1] != '.':
# # print(repr(a4))

#
# a5 = a4.split(". ")
# print('a5:', a5)
# a6 = [x.capitalize() for x in a5]
# a7 = ". ".join(a6)
# print(a7)
# print(a5(0))

#
# b = 0
# while b < len(a5):
#
#         print('qqq', a5(-1)[b-1])
#         a5.strip().lover(a5[b])
#     elif a2(-1)[b-1] == '.':
#         print('www', a5(-1)[b-1])
#
#     else:
#         b = b+1
# print('CAP a5:', a5)

#



# for k in a2:
#     k = k.strip()
#     t = k.capitalize()
# a3 = "\n\t".join(t)
# print(a3)
    # for h in t:
    #     print(h)
    #     h = h.capitalize()
    #     h = h.replace(" iz ", " is ")
    #     print(h)
    #     c = '. '.join(h)
    #     print(c)
# print(a)
# variable = '\n\t'.join(b)
# print(variable)

# print(variable)
# for i in variable:
#     i = i.split('. ')
#     print('i:', i)

        # i = '. '.join(j)

#     i = i.capitalize()
#     i = i.replace(" iz ", " is ")
#     a.append(i)
# variable = '\n\t'.join(a)
#
# # print('Main length:', len(variable))
# #
# cnt = 0
# for i in range(0, len(variable)):
#     if variable[i] in string.whitespace:
#         cnt += 1
#
# print('Count:', cnt)
# print(variable)

# for i in variable:
#     print(i)
