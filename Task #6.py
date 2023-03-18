"""
Create a tool, which will do user generated news feed:

1.User select what data type he wants to add

2.Provide record type required data

3.Record is published on text file in special format



You need to implement:

1.News – text and city as input. Date is calculated during publishing.

2.Privat ad – text and expiration date as input. Day left is calculated during publishing.

3.Your unique one with unique publish rules.

- Promocodes
- Enter Description, link to item, promocode, valid days
- Calculate expiration date

Each new record should be added to the end of file. Commit file in git for review.
"""
from datetime import datetime, timedelta
import os
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
        text

    def get_date(self, text):
        while True:
            if text == 'input':
                print(f'Input {self.date_type} in dd/mm/yyyy format\n')
                text = input()
            else:
                text == text
            try:
                date = datetime.strptime(text, '%d/%m/%Y')
                self.date = date
                break  # valid input received, exit loop
            except ValueError:
                print("Invalid input. Please enter a valid date in dd/mm/yyyy format, or type 'exit' to quit.")
                text = input()
                if text.lower() == 'exit':
                    break  # user chose to exit, exit loop and function

    def get_valid_days(self, text='input'):
        while True:
            if text == 'input':
                print(f'Input {self.date_type} - count of days (use digits, days should be between 0 and 365.)\n')
                text = input()
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

    def promo_code_calc(self):
        self.get_valid_days()
        final_date = (datetime.now() + timedelta(days=int(self.valid_days))).date()
        self.addinfo = f'Proposition valid {self.valid_days} days, actual before: {str(final_date)}'


class ReadFromFile(Publication):

    def __init__(self):
        super().__init__()
        self.default_filename = 'FileForImport.txt'

    def read_file(self):
        date = None
        file_path = input("Please provide file path and filename or press 'Enter' to use default filename ({self.default_filename}): ")
        if not file_path:
            file_path = self.default_filename
        try:
            with open(file_path) as f:
                content = f.read().strip().split('---')
            for line in content:
                fields = line.strip().split(',')
                if fields[0].lower() == 'news':
                    news = AddNews()
                    news.get_publication_body(text=fields[1])
                    news.get_city_and_cur_date(text=fields[2])
                    news.write()
                elif fields[0].lower() == 'adv':
                    adv = AddAdvertisement()
                    adv.get_publication_body(text=fields[1])
                    date = fields[2]
                    # adv.date = date
                    adv.adv_calc(date)
                    adv.write()
                elif fields[0].lower() == 'promocode':
                    promocode = AddPromoCode()
                    promocode.get_publication_body(text=fields[1])
                    valid_days_str = fields[2]
                    valid_days = int(valid_days_str)
                    promocode.get_valid_days(valid_days)
                    promocode.write()
                else:
                    print(f"Invalid record: {line}")
#            os.remove(file_path)  # delete file after reading
        except IOError:
            print("Error reading file")


class Main:
    def __init__(self):
        self.main_message = 'Please choose publication variant:\n1 - for %s\n2 - for %s\n3 - for %s\n4 - to %s\n5 - to %s '% \
                            ('NEWS', 'ADVERTISEMENT', 'PROMOCODE', 'ADD FROM FILE', 'FINISH PROGRAM')
        self.error_message = 'Please make correct choice'
        self.date_error_message = 'Program will be aborted - please enter correct date next time\n'
        pass

    def text_feed_add(self):
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
            return
        else:
            print(self.error_message)
            self.text_feed_add()


if __name__ == "__main__":
    Main().text_feed_add()

