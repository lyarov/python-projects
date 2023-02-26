x = 'x'
d = input("Количество переменных:")
 
z = input("Знак +/-")

ns = []
cs = []
count = []
count1 = []

for i in range(len(ns)):
    print("Степень "+str(i))
    ns[i] = float(input())

for i in range(len(ns)):
    print("Коэфф "+str(i))
    cs[i] = float(input())

for j in range(len(count)):
    if j == 0:
        print("f(x)' = ", end="")
    if cs[j] < 0:
        count1[j] = "0"
    elif ns[j] == 1:
        count[j] = f"{cs[j]} "
        print(count[j], end="")
    else:
        count[j] = f"{ns[j] * cs[j]} {x}^{ns[j] - 1}"
        print(count[j] + z, end="")

for k in range(len(count1)):
    if k == 0:
        print(f"\nf(x)'' = ", end="")
    if cs[k] < 0:
        count1[k] = "0"
        print(count1[k], end="")
    else:
        count1[k] = f"{ns[k] * (ns[k] - 1) * cs[k]} {x}^{ns[k] - 2}"
        print(count1[k] + z, end="")