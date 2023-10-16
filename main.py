import turtle as t

screen = t.Screen()

screen.title("Tic Tac Toe")
screen.bgpic("tic-tac-toe_bg.gif")
screen.screensize(1200, 716)
screen.setup(1235, 741)

turtle = t.Turtle()
turtle.hideturtle()
turtle.pensize(2)
turtle.speed(0)
turtle.pencolor("white")


def draw_X(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(45)
    turtle.pendown()
    turtle.forward(60)
    turtle.backward(120)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.backward(120)
    turtle.penup()


def draw_O(x, y):
    turtle.penup()
    turtle.goto(x, y - 60)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(60)
    turtle.penup()


def get_cell(x, y):
    new_y = 0
    new_x = 0
    cell_x = 0
    cell_y = 1
    for n in range(1, 10):
        cell_x += 1
        if n == 4 or n == 7:
            new_x = 0
            new_y -= 200
            cell_x = 1
            cell_y += 1

        if -368 + new_x <= x <= -137 + new_x and 306 + new_y >= y >= 136 + new_y:
            return -245.0 + new_x, 215.0 + new_y, cell_x, cell_y

        new_x += 231


def game_end(p):
    end_screen = t.Screen()
    end_screen.setup(300, 100)
    end_screen.bgcolor("black")
    end_screen.title(f"{p} wins this")


def is_win(cells, p):
    for column in cells:
        if all(p == cell for cell in column):
            return p
    for n in range(3):
        if all(cells[i][n] == p for i in range(3)):
            return p




def input_in_cell(x, y, grid, inpt):
    grid[x - 1][y - 1] = inpt
    print(grid)


player = 'o'

x_cells = []
o_cells = []
board = [["" for _ in range(3)] for _ in range(3)]


def main(x, y):
    global player

    if len(o_cells) == 5:  # checks for last turn if yes game is ended
        turtle.clear()
        o_cells.clear()
        x_cells.clear()

    co_ords = get_cell(x, y)  # gets cell or_cords from click on screen

    if player == 'o':
        draw_O(co_ords[0], co_ords[1])
        print(co_ords)
        input_in_cell(co_ords[2], co_ords[3], board, "O")
        print(is_win(board, 'O'))
    else:
        draw_X(co_ords[0], co_ords[1])
        x_cells.append([co_ords[2], co_ords[3]])
        print(co_ords)
        input_in_cell(co_ords[2], co_ords[3], board, "X")
        print(is_win(board, 'X'))

    player = "o" if player == 'x' else 'x'


screen.onscreenclick(main)
screen.mainloop()
