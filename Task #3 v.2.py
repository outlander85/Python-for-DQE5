import string
import re
from pydoc import replace

variable = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Calculate the number of whitespace characters
whitespace_count = len(re.findall(r"\s", variable))

counter = 0  # Counter for
variable = variable.lower()  # Making original text in lowercase

# Delete extra line breaks
splitted_text = variable.split("\n")

while counter < len(splitted_text):
    if splitted_text[counter] == '' or splitted_text[counter] == ' ':
        splitted_text.remove(splitted_text[counter])
    else:
        counter = counter + 1

splitted_text = [x.strip() for x in splitted_text]
splitted_text = "\n\t".join(splitted_text)

# Fix 'iz' issue
fixed_text = splitted_text.replace('“iz”', ' “iz”').replace(' iz ', ' is ')


# Creating new additional sentence
sentences = re.split(r'\.\s|\n', fixed_text)
additional_sentence_words = [re.findall(r'\w+$', s)[-1] for s in sentences if re.findall(r'\w+$', s)]
additional_sentence = ' '.join(additional_sentence_words)
fixed_text = fixed_text + ' ' + additional_sentence + '.'

# Creating the final sentence, with the new sentence. + Capitalizing
final_sentence = []

final_list = fixed_text.split('.')

while final_list:
    capitalized_list = final_list.pop(0)
    counter = 0
    for i in capitalized_list:
        if not i.isalpha():
            counter += 1
        elif i == ' ':
            replace(capitalized_list(i), '')
        else:
            break
    capitalized_list = capitalized_list[:counter] + capitalized_list[counter:].capitalize()
    if 'this paragraph' in capitalized_list:
        capitalized_list = capitalized_list + '. ' + additional_sentence
    final_sentence.append(capitalized_list)
final_sentence = '.'.join(final_sentence)
print(final_sentence)

# Calculate the number of whitespace characters in the final text
whitespace_count_final = len(re.findall(r"\s", final_sentence))

print('\n')
print('Number of whitespaces in the original text is:', whitespace_count)
print('Number of whitespaces in the final text is:', whitespace_count_final)
