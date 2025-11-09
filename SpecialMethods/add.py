class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    

vec1 = Vector(1, 2)
vec2 = Vector(3, 4)

vecRes = vec1 + vec2
print(f'{vecRes.x} {vecRes.y}')