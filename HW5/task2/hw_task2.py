import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * from {table_name}')
        self.presidents_data = cursor.fetchall()
        self.presidents_names = [pres[0] for pres in self.presidents_data]
        self.len_ = len(self.presidents_names)
        conn.close()

    def __iter__(self):
        return self

    def __next__(self):
        if self.len_ == 0:
            raise StopIteration
        to_return = {'name': self.presidents_names[self.len_ - 1]}
        self.len_ -= 1
        return to_return

    def __getitem__(self, attr):
        return tuple(filter(lambda president: attr in president, self.presidents_data))[0]

    def __len__(self):
        return self.len_

    def __contains__(self, item):
        return item in self.presidents_names
