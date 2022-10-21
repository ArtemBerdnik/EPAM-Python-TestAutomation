import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        print("Initiate a new TableData object")
        print(f"Connecting to {database_name}")
        print(f"Trying to fetch data from {table_name}")
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * from {table_name}')
        self.database_name = database_name
        self.table_name = table_name
        self.presidents_data = cursor.fetchall()
        self.presidents_names = [pres[0] for pres in self.presidents_data]
        self.len_ = len(self.presidents_names)
        conn.close()

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

    @staticmethod
    def update_data_in_table(president_name: str, age_of_president: int, country: str) -> None:
        conn = sqlite3.connect('HW5/task2/example.sqlite')
        cursor = conn.cursor()
        cursor.execute(f"insert into presidents values ('{president_name}', {age_of_president}, '{country}')")
        conn.commit()
        conn.close()

    @staticmethod
    def delete_data_in_table(table_name: str, field: str, field_value: str) -> None:
        conn = sqlite3.connect('HW5/task2/example.sqlite')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name} where {field} = '{field_value}'")
        conn.commit()
        conn.close()
