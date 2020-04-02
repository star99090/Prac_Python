import turtle
t = turtle.Pen()

while True:
    direction=input("왼쪽=left, 오른쪽=right : ")
    if direction=="left":
        t.left(60)
        t.forward(100)
    if direction=="right":
        t.right(60)
        t.forward(100)
    if direction=="back":
        t.backward(100)
    if direction=="head":
        t.forward(100)
