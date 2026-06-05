class ChairType():
    def __init__(self, type, color):
        self.type = type
        self.color = color
    def display(self, x, y):
        print(f"Легкий {self.type} ({self.color}) летит в Мишу в точке ({x}, {y})")

class ChairCreator():
    _chair_type = {}
    @classmethod
    def create_chair(cls, type, color):
        key = (type, color)
        if key not in cls._chair_type:
            cls._chair_type[key] = ChairType(type, color)
        return cls._chair_type[key]

class Chair:
    def __init__(self, x, y, type : ChairType):
        self.x = x
        self.y = y
        self.type = type
    def fly(self):
        self.type.display(self.x, self.y)
