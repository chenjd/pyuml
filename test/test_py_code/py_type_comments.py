class MovementObject:
    def __init__(self):
        pass


class Car(MovementObject):
    def __init__(self):
        self.num_one = 1  # type: int
        self.num_two = 2.0  # type: float
        self.name = "car"  # type: str

    def get_user_name(self,
                      user_id,  # type: int
                      ):  # type: str
        return 'car'


class Car2(Car):
    def __init__(self):
        self.num_one = 1  # type: int
        self.num_two = 2.0  # type: float
        self.name = "car2"  # type: str

    def get_user_name(self,
                      user_id,  # type: int
                      ):  # type: str
        return 'car2'


class Car3(Car, MovementObject):
    def __init__(self):
        self.num_one = 1  # type: int
        self.num_two = 2.0  # type: float
        self.name = "car3"  # type: str

    def get_user_name(self,
                      user_id,  # type: int
                      ):  # type: str
        return 'car3'

    def greeting(self,
                 user_id,  # type: int
                 content,  # type: str
                 ):  # type: str
        return 'Hello ' + self.get_user_name(user_id) + content
