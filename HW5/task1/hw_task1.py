class KeyValueStorage:

    def __init__(self, data):
        self.data = data
        with open(data, 'r') as d:
            for line in d:
                key_and_value = line.split("=")
                if key_and_value[0].isdigit():
                    raise ValueError('int value can not be a key in dict')
                setattr(self, key_and_value[0], int(key_and_value[1].rstrip())) if key_and_value[1].rstrip().isdigit() \
                    else setattr(self, key_and_value[0], key_and_value[1].rstrip())

    def __getitem__(self, attr):
        return self.__dict__[attr]