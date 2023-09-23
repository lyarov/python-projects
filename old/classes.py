class P2A():
    def __init__(self):
        self.group = "P2A"


ilya = P2A()

ilya.name = "Ilya"
ilya.surname = "Fedorov"
ilya.age = 17
ilya.male = True

print(ilya.group)

for s in range(3):
    s = P2A()
    s.name = input(f"{s} name: ")
    s.surname = input("surname: ")
    s.age = input("age: ")
    s.male = True

for s in range(3):
    print(s.name)
    print(s.surname)
    print(s.age)
    print(s.age)
    print(s.male) 