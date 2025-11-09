class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def __repr__(self):
        return f"{self.title} in {self.year}"
    
    def __str__(self):
        return f"{self.title} by {self.author} in {self.year}"
    

b = Book("Fundamentals of python", 1994, "Guido van Rossum")

print(repr(b))
print(b)

#If __str__ is missing then it will fallback to either __repr__