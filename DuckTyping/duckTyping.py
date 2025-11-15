class Duck:
    def quack(self):
        print('Duck is quacking')
    
    def walk(self):
        print('Walks like a duck')


class SimulateDuck:
    def quack(self):
        print("imitating a duck's quack")

    def walk(self):
        print("imitating a duck's walk")

lstObjs = [Duck(), SimulateDuck()]

for obj in lstObjs:
    obj.walk()

#NOTE: duck typing is used with/without inheritance.