import string
import re

variable = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


a = 0
variable = variable.lower()
# print('variable:', repr(variable))

# Delete multi-\n's
a2 = variable.split("\n")
# print('a2:', a2)
while a < len(a2):
    if a2[a] == '' or a2[a] == ' ':
        a2.remove(a2[a])
    else:
        a = a+1
# print('Modified a2:', a2)

a3 = [x.strip().capitalize() for x in a2]
# print('a3:', a3)

a4 = "\n\t".join(a3)
# print('a4:', a4)
# print('a4:', repr(a4))

a5 = a4.replace('“iz”', ' “iz”').replace(' iz ', ' is ')
# print('a5:', a5)

additional_sentence_words = []
a6 = a5.split()
# print('a6:', a6)

for i in range(len(a6)):
    if re.findall('[.!?]', a6[i]):
        additional_sentence_words.append(re.sub('[.!?]', '', a6[i]))
additional_sentence = ' '.join(additional_sentence_words).capitalize() + '.'
# print(additional_sentence)

final_sentence = a5 + ' \n\t' + additional_sentence
print(final_sentence)

cnt = 0
for i in range(0, len(final_sentence)):
    if final_sentence[i] in string.whitespace:
        cnt += 1

print('\nNumber of whitespaces is:', cnt)

