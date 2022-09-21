import turtle as t



screen = t.Screen()
t.up()
t.addshape("wordlechart.gif")
t.bgpic("wordlechart.gif")

t.goto(-82.5,201)
t.write("Wordle",font=("Georgia",40,"bold"))
t.ht()
t.goto(-160,136)
xcor = t.xcor()
ycor = t.ycor()

print(xcor,ycor)
#-165,200 (first pixel of left top corner)
accum = 0
def w():
    xcor = open("xcor.txt","r+")
    ycor = open("ycor.txt","r+")
    accum = open("accum.txt","r+")
    t.goto(xcor.read(),ycor.read())
    t.write("W",font=("Helvetica Neue",40))
    
    xcor += 57
    accum += 1
            
screen.onkeypress(w,"w")
screen.listen()

t.done()
#57 width (box)
# +5 off X, -5 off Y (at start of white box on bottom corner not gray) for perfect letter placement
#57 length (box)