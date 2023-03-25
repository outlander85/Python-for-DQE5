import pyodbc

class DatabaseManager:
    def __init__(self):
        self.connection = pyodbc.connect('Driver={SQLite3 ODBC Driver};'
                                         'Direct=True;'
                                         'Database=newsfeed11.db;'
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
        columns = self.tables[table_name]
        placeholders = ', '.join(['?' for _ in columns])
        values = [getattr(record, column) for column in columns]
        query = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})'
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


db = DatabaseManager()
db.create_news_table()
db.create_advertisement_table()
db.create_promocode_table()
db.close_connection()