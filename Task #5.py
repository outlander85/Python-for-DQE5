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


class Publication:

    def __init__(self):
        pass

    def variant(self, variant):
        pass


class Input:

    def __init__(self):
        pass

    def choose_input_mode(self):
        choose = ''
        print('Please choose publication variant:\n1 - for %s\n2 - for %s\n3 - for %s' %
              ('NEWS', 'ADVERTISEMENT', 'PROMOCODE'))
        try:
            choose = int(input())
        except ValueError:
            print("You've entered wrong value")

        if choose == 1:
            mode = 'NEWS'
        elif choose == 2:
            mode = 'ADVERTISEMENT'
        elif choose == 3:
            mode = 'PROMOCODE'
        else:
            # print('Please make correct choice')
            mode = None

        if choose in (1, 2, 3):
            print(f"You've chosen {mode}")
        else:
            print('Please make correct choice')

        return choose

    def input_news(self):
        pass

    def input_adv(self):
        pass


class Calc:
    pass


class AddNews(Publication):
    pass


class AddAdvertisement:
    pass


class AddPromoCode:
    pass


class WriteLog:
    pass


Input.choose_input_mode(self=None)
print(Input.choose_input_mode.choose)
