length = int(input("Введите длину массива: "))

grades = []

for i in range(length):
    number = int(input(f"Введите число {i + 1}: "))
    grades.append(number)

print("Заполненный массив:", grades)

threes = []
fours = []

for grade in grades:
    if grade % 2 == 0:
        fours.append(grade)
    else:
        threes.append(grade)

print(" ".join(str(x) for x in threes))
print(" ".join(str(x) for x in fours))

if len(fours) >= len(threes):
    print("YES")
else:
    print("NO")