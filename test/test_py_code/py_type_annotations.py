class MovementObject:
    def __init__(self):
        pass


class Car(MovementObject):
    def __init__(self):
        self.num_one: int = 1
        self.num_two: float = 2.0
        self.name: str = "car"

    def get_user_name(self, user_id: int) -> str:
        return 'car'


class Car2(Car):
    def __init__(self):
        self.num_one: int = 1
        self.num_two: float = 2.0
        self.name: str = "car2"

    def get_user_name(self, user_id: int) -> str:
        return 'car2'


class Car3(Car, MovementObject):
    def __init__(self):
        self.num_one: int = 1
        self.num_two: float = 2
        self.name: str = "car3"

    def get_user_name(self, user_id: int) -> str:
        return 'car2'

    def greeting(self, user_id: int, content: str) -> str:
        return 'Hello ' + self.get_user_name(user_id) + content
