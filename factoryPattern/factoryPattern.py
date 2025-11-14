class Shape:
    @classmethod
    def create(sides):
        if sides == 3:
            return Triangle()
        elif sides == 4:
            return Square()
        else:
            raise TypeError("Type not supported.")
        

class Triangle:
    pass

class Square:
    pass