import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title("Tower of Hanoi")

hanoi_turtle = turtle.Turtle()
hanoi_turtle.speed(0)  # Set the drawing speed


def draw_disk(width, height):
    hanoi_turtle.penup()
    hanoi_turtle.goto(-width / 2, -150 - height)
    hanoi_turtle.pendown()
    hanoi_turtle.begin_fill()
    for _ in range(2):
        hanoi_turtle.forward(width)
        hanoi_turtle.left(90)
        hanoi_turtle.forward(20)
        hanoi_turtle.left(90)
    hanoi_turtle.end_fill()
    hanoi_turtle.penup()
    hanoi_turtle.goto(0, -150)


def draw_tower(tower, x, width):
    for i, disk in enumerate(tower):
        draw_disk(width - disk * 20, i * 20)


def draw_hanoi(towers):
    hanoi_turtle.clear()
    for i in range(3):
        x = i * 200 - 200
        draw_tower(towers[i], x, 200)


def tower_of_hanoi(n, source, auxiliary, target):
    if n > 0:

        tower_of_hanoi(n - 1, source, target, auxiliary)

        target.append(source.pop())

        draw_hanoi(towers)
        window.update()

        tower_of_hanoi(n - 1, auxiliary, source, target)


towers = [[], [], []]
n_disks = 4

for i in range(n_disks, 0, -1):
    towers[0].append(i)

draw_hanoi(towers)
window.update()

tower_of_hanoi(n_disks, towers[0], towers[1], towers[2])

window.exitonclick()
