import turtle
if __name__ == '__main__':
    """dank drawn"""
    turtle.shape("turtle")
def to_center():
    turtle.right(360)
    turtle.backward(50)
    turtle.left(90)
    turtle.backward(50)
def wing():
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
"""To center"""
to_center()
"""Second wing"""
wing()
"""To center"""
to_center()
wing()
to_center()
wing()
turtle.exitonclick()