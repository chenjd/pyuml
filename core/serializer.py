import shelve


class Serializer:
    def __init__(self):
        pass

    def serialize(self, obj):
        with shelve.open('ast.db') as db:
            db['eggs'] = 'eggs'

    def deserilize(self):
        with shelve.open('ast.db') as db:
            print(db['eggs'])


