import turtle

# Создаем объект Turtle
t = turtle.Turtle()
t.speed(0)  # Устанавливаем максимальную скорость для рисования

for i in range(0, 70):
    t.color("white")
    t.circle(size)
    t.left(5)
    size = size + 3


# Закрытие окна по щелчку
turtle.exitonclick()
