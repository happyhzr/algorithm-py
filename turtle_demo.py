import turtle


def draw_spiral(my_turtle: turtle.Turtle, line_len: float):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len=line_len - 5)


if __name__ == "__main__":
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    draw_spiral(my_turtle, 100)
    my_win.exitonclick()
