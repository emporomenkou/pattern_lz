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

def main():
    print("\nЛегковес:\n")
    misha = []
    type_chair = ChairCreator.create_chair("chair", "korichnevi")
    type_armchair = ChairCreator.create_chair("armchair", "chorni")

    misha.append(Chair(228, 1337, type_chair))
    misha.append(Chair(67, 69, type_chair))
    misha.append(Chair(0, 1, type_chair))

    misha.append(Chair(2, 3, type_armchair))    
    misha.append(Chair(6767, 6969, type_armchair))
    misha.append(Chair(228228, 13371337, type_armchair))

    for chair in misha:
        chair.fly()
    
if __name__ == "__main__":
    main()