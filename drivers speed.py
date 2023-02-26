
while(True):
    
    speed = int(input("Скорость водителя: "))
    overspeed = speed - 60
    
    if(speed >=61 and speed <=200):
        print("Водитель нарушает. Превышение скорости на", overspeed, "км/ч")
    elif(speed >=200):
        print("Водитель не ракета. Превышение на", overspeed, "км/ч")
    else:
        print("Водитель не нарушает. Скорость:", speed, "км/ч")
        

    
