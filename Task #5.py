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
            text = input()
        self.article_body = text

    def get_city_and_cur_date(self, text='input'):
        if text == 'input':
            print(f'Input city\n')
            text = input()
        self.addinfo = text + ', ' + str(datetime.now())

    def get_date(self, text='input'):
        if text == 'input':
            print(f'Input {self.date_type} in dd/mm/yyyy format\n')
            text = input()
        self.date = text

    def get_valid_days(self, text='input'):
        if text == 'input':
            print(f'Input {self.date_type} - count of days (use digits)\n')
            text = input()
        self.valid_days = text

    def write(self):
        f = open(os.path.abspath('LOG.txt'), 'a')
        f.write('\n'.join([self.header, self.article_body, self.addinfo, '\n----\n\n']))
        f.close()


class AddNews(Publication):

    def __init__(self):
        super().__init__()
        self.header = 'News:'
        self.article_type = 'News'


class AddAdvertisement(Publication):

    def __init__(self):
        super().__init__()
        self.header = 'Advertisement:'
        self.article_type = 'Adv'
        self.date_type = 'Exp.date'

    def adv_calc(self):
        self.get_date()
        days = datetime.date(datetime.strptime(self.date, '%d/%m/%Y')) - datetime.date(datetime.now())
        self.addinfo = f'Actual until: {self.date}, {days.days} days left'


class AddPromoCode(Publication):

    def __init__(self):
        super().__init__()
        self.header = 'New PromoCode'
        self.type = 'PromoCode'
        self.date_type = 'Valid days'

    def promo_code_calc(self):
        self.get_valid_days()
        final_date = datetime.date(datetime.now()) + timedelta(days=int(self.valid_days))
        self.addinfo = f'Proposition valid {self.valid_days} days, actual before: {str(final_date)}'


class Main:
    def __init__(self):
        self.main_message = 'Please choose publication variant:\n1 - for %s\n2 - for %s\n3 - for %s\n4 - to %s' % \
                            ('NEWS', 'ADVERTISEMENT', 'PROMOCODE', 'FINISH PROGRAM')
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
            return
        else:
            print(self.error_message)
            self.text_feed_add()


if __name__ == "__main__":
    Main().text_feed_add()

