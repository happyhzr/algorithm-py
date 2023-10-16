import turtle


def tree(branch_len: float, t: turtle.Turtle):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)


if __name__ == "__main__":
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("black")
    tree(110, t)
    my_win.exitonclick()
