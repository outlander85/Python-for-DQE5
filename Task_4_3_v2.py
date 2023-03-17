import re
from pydoc import replace

class TextNormalizer:
    def __init__(self, text):
        self.text = text

    def normalize_case(self):
        self.text = self.text.lower()

    def delete_extra_line_breaks(self):
        splitted_text = self.text.split("\n")
        splitted_text = [x.strip() for x in splitted_text if x.strip()]
        self.text = "\n\t".join(splitted_text)

    def fix_iz_issue(self):
        self.text = self.text.replace('“iz”', ' “iz”').replace(' iz ', ' is ')

    def create_additional_sentence(self):
        sentences = re.split(r'\.\s|\n', self.text)
        additional_sentence_words = [re.findall(r'\w+$', s)[-1] for s in sentences if re.findall(r'\w+$', s)]
        additional_sentence = ' '.join(additional_sentence_words)
        self.text = self.text + ' ' + additional_sentence + '.'

    def capitalize_sentences(self):
        final_sentence = []
        final_list = self.text.split('.')
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
                capitalized_list = capitalized_list + '.'
            final_sentence.append(capitalized_list)
        self.text = '.'.join(final_sentence)

    def get_normalized_text(self):
        self.normalize_case()
        self.delete_extra_line_breaks()
        self.fix_iz_issue()
        #self.create_additional_sentence()
        self.capitalize_sentences()
        return self.text

    def count_whitespaces(self):
        return len(re.findall(r"\s", self.text))

variable = """homEwork:
    tHis iz your homeWork, copy these Text to variable. 

    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

    last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

#normalizer = TextNormalizer(variable)
#normalized_text = normalizer.get_normalized_text()
#whitespace_count = normalizer.count_whitespaces()
#print(normalized_text)
#print('Number of whitespaces in the text is:', whitespace_count)