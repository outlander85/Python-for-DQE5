"""
Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:

1.Define your input format (one or many records)

2.Default folder or user provided file path

3.Remove file if it was successfully processed
"""
from datetime import datetime, timedelta
import os
import json
import csv
import xml.etree.ElementTree as ET
from collections import Counter
import re
from Task_4_3_v2 import TextNormalizer as norm


class Publication:
    def __init__(self):
        self.header = ''
        self.article_type = ''
        self.date_type = ''
        self.article_body = ''
        self.date = ''
        self.valid_days = ''
        self.addinfo = ''

    def get_publication_body(self, text='input'):
        if text == 'input':
            print(f'Input {self.article_type} body\n')
            text = norm(input()).get_normalized_text()
        self.article_body = text

    def get_date(self, text):
        while True:
            if text == 'input':
                print(f'Input {self.date_type} in dd/mm/yyyy format\n')
                text = input()
            else:
                text
            try:
                date = datetime.strptime(text, '%d/%m/%Y')
                self.date = date
                break  # valid input received, exit loop
            except ValueError:
                print("Invalid input. Please enter a valid date in dd/mm/yyyy format, or type 'exit' to quit.")
                text = input()
                if text.lower() == 'exit':
                    break  # user chose to exit, exit loop and function

    def get_valid_days(self, text):
        while True:
            if text == 'input':
                print(f'Input {self.date_type} - count of days (use digits, days should be between 0 and 365.)\n')
                text = input()
            else:
                text
            try:
                days = int(text)
                if days < 0 or days > 365:
                    raise ValueError("Days should be between 0 and 365.")
                self.valid_days = days
                break  # valid input received, exit loop
            except ValueError:
                print("Invalid input. Please enter a valid number of days between 0 and 365, or type 'exit' to quit.")
                text = input()
                if text.lower() == 'exit':
                    break  # user chose to exit, exit loop and function

    def write(self):
        f = open(os.path.abspath('newsfeed.txt'), 'a')
        f.write('\n'.join([self.header, self.article_body, self.addinfo, '------------------------------\n\n\n']))
        f.close()


class TextAnalyzer:
    def __init__(self):
        self.word_count = 0
        self.letter_count = 0
        self.uppercase_count = 0

    def analyze_text(self, text):
        # Calculate word count and letter count
        words = re.findall(r'\b\w+\b', text.lower())  # find all words in text
        words = [word for word in words if not word.isdigit()]  # exclude words that only contain digits
        word_count = len(words)
        letter_count = sum(len(word) for word in words)

        # Calculate uppercase count
        uppercase_count = sum(1 for c in text if c.isupper())

        # Count the frequency of each word
        word_freq = Counter(words)

        # Create a list of tuples containing distinct word and its count
        word_count_list = [(word, count) for word, count in word_freq.items()]

        # Sort the list alphabetically by word
        word_count_list.sort(key=lambda x: x[0])

        return word_count_list

    def create_word_count_csv(self, filename, word_count_list):
        # Create csv file with word count
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter='-')
            writer.writerows(word_count_list)

    def create_letter_count_csv(self, filename, text):
        # Create csv file with letter count
        lowercase_text = text.lower()  # convert to lowercase
        letters = set(c for c in lowercase_text if c.isalpha())
        total_count = sum(1 for c in lowercase_text if c.isalpha())
        uppercase_count = sum(1 for c in text if c.isupper())
        lowercase_count = total_count - uppercase_count

        rows = []
        for letter in sorted(letters):
            count = sum(1 for c in lowercase_text if c == letter)
            uppercase = sum(1 for c in text if c == letter and c.isupper())
            percentage = round(count / total_count * 100, 2)
            row = {'Letter': letter, 'Count_all': count, 'Count_uppercase': uppercase, 'Percentage': percentage}
            rows.append(row)

        fieldnames = ['Letter', 'Count_all', 'Count_uppercase', 'Percentage']
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def write_csv(self, filename='newsfeed.txt'):
        with open(filename, 'r') as article_body:
            text = article_body.read()
            lines = text.split('\n')
        analyzer = TextAnalyzer()
        words = analyzer.analyze_text(text)

        # Create word count csv
        word_count_file = os.path.abspath('word-count.csv')
        analyzer.create_word_count_csv(word_count_file, words)

        # Create letter count csv
        letter_count_file = os.path.abspath('letter-count.csv')
        analyzer.create_letter_count_csv(letter_count_file, text)

class AddNews(Publication):

    def __init__(self):
        super().__init__()
        self.header = 'News -------------------------'
        self.article_type = 'News'

    def get_city_and_cur_date(self, text='input'):
        if text == 'input':
            print(f'Input city\n')
            text = norm(input()).get_normalized_text()
        self.addinfo = text + ', ' + str(datetime.now().strftime("%d/%m/%Y %H.%M"))


class AddAdvertisement(Publication):

    def __init__(self):
        super().__init__()
        self.header = 'Advertisement ----------------'
        self.article_type = 'Adv'
        self.date_type = 'Exp.date'

    def adv_calc(self, text='input'):
        self.get_date(text)
        days = self.date - datetime.now()
        self.addinfo = f'Actual until: {self.date.strftime("%d/%m/%Y")}, {days.days} days left'


class AddPromoCode(Publication):

    def __init__(self):
        super().__init__()
        self.header = 'PromoCode --------------------'
        self.type = 'PromoCode'
        self.date_type = 'Valid days'

    def promo_code_calc(self, text='input'):
        self.get_valid_days(text)
        final_date = (datetime.now() + timedelta(days=int(self.valid_days))).date()
        self.addinfo = f'Proposition will be valid for {self.valid_days} days, actual before: {str(final_date.strftime("%d/%m/%Y"))}'


class ReadFromFile(Publication):

    def __init__(self):
        super().__init__()
        self.default_filename = 'FileForImport.txt'

    def read_file(self):
        file_path = input(f"Please provide file path and filename or press 'Enter' to use default filename ({self.default_filename}): ")
        if not file_path:
            file_path = self.default_filename
        try:
            with open(file_path) as f:
                num_rows = input("Please enter the number of rows to import (or press 'Enter' for all rows): ")
                content = f.read().strip().split('---')
            if num_rows:
                content = content[:int(num_rows)]
            for line in content:
                fields = line.strip().split(',')
                if fields[0].lower() == 'news':
                    news = AddNews()
                    news.get_publication_body(text=norm(fields[1]).get_normalized_text())
                    news.get_city_and_cur_date(text=fields[2])
                    news.write()
                elif fields[0].lower() == 'adv':
                    adv = AddAdvertisement()
                    adv.get_publication_body(text=norm(fields[1]).get_normalized_text())
                    date = fields[2]
                    adv.adv_calc(date)
                    adv.write()
                elif fields[0].lower() == 'promocode':
                    promocode = AddPromoCode()
                    promocode.get_publication_body(text=norm(fields[1]).get_normalized_text())
                    valid_days = fields[2]
                    promocode.promo_code_calc(valid_days)
                    promocode.write()
                else:
                    print(f"Invalid record: {line}")
            os.remove(file_path)  # delete file after reading
        except IOError:
            print("Error reading file")
        except IndexError:
            print(f"Something wrong with '{file_path}' file, please check and fix it or choose the correct one.")


class ReadFromJSON(Publication):

    def __init__(self):
        super().__init__()
        self.default_json_filename = 'JSONForImport.json'

    def read_json(self):
        file_path = input(f"Please provide JSON file path and filename or press 'Enter' to use the default filename ({self.default_json_filename}): ")
        if not file_path:
            file_path = self.default_json_filename

        try:
            with open(file_path) as f:
                num_rows = input("Please enter the number of rows to import (or press 'Enter' for all rows): ")
                data = json.load(f)
                records = data.get('records')
                if num_rows:
                    records = records[:int(num_rows)]
                for record in records:
                    if record.get('type').lower() == 'news':
                        news = AddNews()
                        news.get_publication_body(text=norm(record.get('body')).get_normalized_text())
                        news.get_city_and_cur_date(text=record.get('location'))
                        news.write()
                    elif record.get('type').lower() == 'adv':
                        adv = AddAdvertisement()
                        adv.get_publication_body(text=norm(record.get('body')).get_normalized_text())
                        date = str(record.get('date'))
                        adv.adv_calc(date)
                        adv.write()
                    elif record.get('type').lower() == 'promocode':
                        promocode = AddPromoCode()
                        promocode.get_publication_body(text=norm(record.get('body')).get_normalized_text())
                        valid_days = str(record.get('valid_days'))
                        promocode.promo_code_calc(valid_days)
                        promocode.write()
                    else:
                        print(f"Invalid record: {record}")
            os.remove(file_path)  # delete file after reading
        except IOError:
            print("Error reading file")
        except json.decoder.JSONDecodeError:
            print(f"Something wrong with '{file_path}' file, please check and fix it or choose the correct one.")


class ReadFromXML(Publication):
    def __init__(self):
        super().__init__()
        self.default_xml_filename = 'XMLForImport.xml'

    def read_xml(self):
        file_path = input(f"Please provide XML file path and filename or press 'Enter' to use the default filename ({self.default_xml_filename}): ")
        if not file_path:
            file_path = self.default_xml_filename

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            num_rows = input("Please enter the number of rows to import (or press 'Enter' for all rows): ")
            records = root.findall('record')
            if num_rows:
                records = records[:int(num_rows)]
            for record in records:
                record_type = record.find('type').text.lower()
                record_body = norm(record.find('body').text).get_normalized_text()
                if record_type == 'news':
                    news = AddNews()
                    news.get_publication_body(text=record_body)
                    news.get_city_and_cur_date(text=record.find('location').text)
                    news.write()
                elif record_type == 'adv':
                    adv = AddAdvertisement()
                    adv.get_publication_body(text=record_body)
                    date = str(record.find('date').text)
                    adv.adv_calc(date)
                    adv.write()
                elif record_type == 'promocode':
                    promocode = AddPromoCode()
                    promocode.get_publication_body(text=record_body)
                    valid_days = str(record.find('valid_days').text)
                    promocode.promo_code_calc(valid_days)
                    promocode.write()
                else:
                    print(f"Invalid record: {record}")
#            os.remove(file_path)  # delete file after reading
        except IOError:
            print("Error reading file")
        except AttributeError:
            print(f"Something wrong with '{file_path}' file structure, please check and fix it or choose the correct one.")
        except ET.ParseError:
            print(f"Something wrong with '{file_path}' file, please check and fix it or choose the correct one.")


class Main:
    def __init__(self):
        self.main_message = 'Please choose publication variant:\n1 - for %s\n2 - for %s\n3 - for %s\n4 - to %s\n5 - to %s\n6 - to %s\n7 - to %s '% \
                            ('NEWS', 'ADVERTISEMENT', 'PROMOCODE', 'ADD FROM FILE', 'ADD FROM JSON', 'ADD FROM XML', 'FINISH PROGRAM')
        self.error_message = 'Please make correct choice'
        self.date_error_message = 'Program will be aborted - please enter correct date next time\n'
        pass

    def text_feed_add(self):
        textanalyzer = TextAnalyzer()
        print(self.main_message)
        choice = input()
        if choice == '1':
            news = AddNews()
            news.get_publication_body()
            news.get_city_and_cur_date()
            news.write()
            self.text_feed_add()
        elif choice == '2':
            adv = AddAdvertisement()
            adv.get_publication_body()
            try:
                adv.adv_calc()
                adv.write()
            except ValueError:
                print(self.date_error_message)
            finally:
                self.text_feed_add()
        elif choice == '3':
            promocode = AddPromoCode()
            promocode.get_publication_body()
            try:
                promocode.promo_code_calc()
                promocode.write()
            except ValueError:
                print(self.date_error_message)
            finally:
                self.text_feed_add()
        elif choice == '4':
            addfromfile = ReadFromFile()
            addfromfile.read_file()
            self.text_feed_add()
        elif choice == '5':
            addfromjson = ReadFromJSON()
            addfromjson.read_json()
            self.text_feed_add()
        elif choice == '6':
            addfromxml = ReadFromXML()
            addfromxml.read_xml()
            self.text_feed_add()
        elif choice == '7':
            return
        else:
            print(self.error_message)
            self.text_feed_add()
        textanalyzer.write_csv()

if __name__ == "__main__":
    Main().text_feed_add()

