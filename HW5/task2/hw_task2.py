import contextlib
import sqlite3


@contextlib.contextmanager
def get_cursor_in_db(db):
    conn = sqlite3.connect(db)
    try:
        yield conn.cursor()
    finally:
        conn.commit()
        conn.close()


class TableData:
    presidents_data = set()

    def __init__(self, database_name, table_name):
        with get_cursor_in_db(database_name) as cursor:
            cursor.execute(f'SELECT * from {table_name}')
            for entry in cursor:
                self.presidents_data.add(entry)
        self.database_name = database_name
        self.table_name = table_name
        self.presidents_names = [pres[0] for pres in self.presidents_data]
        self.len_ = len(self.presidents_names)

    def __iter__(self):
        self.__init__(self.database_name, self.table_name)
        return self

    def __next__(self):
        if self.len_ == 0:
            raise StopIteration
        to_return = {'name': self.presidents_names[self.len_ - 1]}
        self.len_ -= 1
        return to_return

    def __getitem__(self, attr):
        print(f"Getting item {attr}")
        self.__init__(self.database_name, self.table_name)
        return tuple(filter(lambda president: attr in president, self.presidents_data))[0]

    def __len__(self):
        print(f"Getting length of an TableData object")
        self.__init__(self.database_name, self.table_name)
        return self.len_

    def __contains__(self, item):
        print(f"Checking if a TableData object contains '{item}'")
        self.__init__(self.database_name, self.table_name)
        return item in self.presidents_names
