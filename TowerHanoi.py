import turtle

# Set up the Turtle screen
window = turtle.Screen()
window.bgcolor("white")
window.title("Tower of Hanoi")

# Create a Turtle object
hanoi_turtle = turtle.Turtle()
hanoi_turtle.speed(0)  # Set the drawing speed

# Function to draw a single disk


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

# Function to draw a tower


def draw_tower(tower, x, width):
    for i, disk in enumerate(tower):
        draw_disk(width - disk * 20, i * 20)

# Function to draw the entire Tower of Hanoi


def draw_hanoi(towers):
    hanoi_turtle.clear()
    for i in range(3):
        x = i * 200 - 200
        draw_tower(towers[i], x, 200)

# Tower of Hanoi algorithm


def tower_of_hanoi(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        tower_of_hanoi(n - 1, source, target, auxiliary)

        # Move the nth disk from source to target peg
        target.append(source.pop())

        # Display the current state of the towers
        draw_hanoi(towers)
        window.update()

        # Move the n-1 disks from auxiliary peg to target peg
        tower_of_hanoi(n - 1, auxiliary, source, target)


# Initialize towers and number of disks
towers = [[], [], []]
n_disks = 4

# Add the disks to the source tower
for i in range(n_disks, 0, -1):
    towers[0].append(i)

# Draw the initial state of the towers
draw_hanoi(towers)
window.update()

# Call the Tower of Hanoi algorithm to solve the puzzle
tower_of_hanoi(n_disks, towers[0], towers[1], towers[2])

# Close the window when done
window.exitonclick()
