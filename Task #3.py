"""
homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
# --------------------------------------------------------------------------------------------------------------------------------------------------------
variable = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

import string
import re
a = []
b = []
c = []

# print(variable)
# variable = variable.replace(" iz ".lower(), " is ")
variable = variable.replace("\n\n", "\n")
# variable = ' '.join(variable.split())

"""
variable = variable.split("\t")
for i in variable:
    # variable = variable.replace("\t", "")
    i = i.replace("\n", "")
    a.append(i)
print(variable)
"""
a2 = variable.split("\n\t")
a3 = [x.capitalize() for x in a2]
a4 = "\n\t".join(a3)

a5 = a4.split(". ")
a6 = [x.capitalize() for x in a5]
a7 = ". ".join(a6)
print(a6)


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
