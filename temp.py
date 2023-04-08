import pyodbc
from datetime import datetime, timedelta

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
            text = 'test1'
        self.article_body = text
        print(news.article_body)
        print(news.addinfo)

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


class DatabaseManager:
    def __init__(self):
        self.connection = pyodbc.connect('Driver={SQLite3 ODBC Driver};'
                                         'Direct=True;'
                                         'Database=newsfeed.db;'
                                         'String Types=Unicode', autocommit=True)
        self.cursor = self.connection.cursor()
        self.tables = {}
        self.query = ()

    def create_table(self, table_name, columns):
        columns_str = ', '.join([f'{name} {datatype}' for name, datatype in columns.items()])
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})'
        print(query)
        self.cursor.execute(query)
        self.tables[table_name] = list(columns.keys())
        print(table_name)

    def close_connection(self):
        self.connection.close()

    def insert_record(self, record):
        table_name = record.article_type.lower()
        print(f'table_name: {table_name}')
        columns = self.tables[table_name]
        print(f'columns: {columns}')
        placeholders = ', '.join(['?' for _ in columns])
        print(f'placeholders: {placeholders}')
        print(record)
        print(columns)
        values = [getattr(record, column) for column in columns]
        print(f'values: {values}')
        query = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})'
        print(query)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print('Record added successfully!')
        except pyodbc.IntegrityError:
            print('Record already exists in the database!')

    def create_news_table(self):
        self.create_table('news', {
            'Body': 'TEXT',
            'City': 'TEXT',
            'Date': 'TEXT'
        })

    def create_advertisement_table(self):
        self.create_table('advertisement', {
            'Body': 'TEXT',
            'Actual_until_date': 'TEXT',
            'Days_left': 'TEXT'
        })

    def create_promocode_table(self):
        self.create_table('promocode', {
            'Body': 'TEXT',
            'Valid_days': 'TEXT',
            'Actual_before_date': 'TEXT'
        })



class AddNews(Publication):
    def __init__(self):
        super().__init__()
        self.header = 'News -------------------------'
        self.article_type = 'News'
        self.Body = ''
        self.City = ''
        self.Date = ''

    def get_city_and_cur_date(self, text='input'):
        if text == 'input':
            print(f'Input city\n')
            text = 'Test'
        self.City = text
        self.Date = str(datetime.now().strftime("%d/%m/%Y %H.%M"))


    def write(self):

        # Create needed tables
        db = DatabaseManager()
        db.create_news_table()
        db.create_advertisement_table()
        db.create_promocode_table()

        # Add a record to the database
        db.insert_record(self)
        db.close_connection()


news = AddNews()
news.get_publication_body()
news.get_city_and_cur_date()
news.write()