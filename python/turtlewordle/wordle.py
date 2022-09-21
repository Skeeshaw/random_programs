import turtle as t
import time
#cant automate these cause they dont follow the same naming scheme
t.addshape("wordlebox - Copy.gif")

accum = 2

#automate shape creation
for shapecreate in range(28):
    t.addshape("wordlebox - Copy ("+str(accum)+").gif")
    print("Added shape: Copy",str(accum))
    accum += 1
    
#setup
t.up()
#t.speed(0)
#t.delay(0)
t.goto(-171,202)

#setting coords of first shape
worldedistance_X = -171
worldedistance_Y = 202

#reset accum
accum = 2

t.shape("wordlebox - Copy.gif")
time.sleep(2)
t.goto(200,100)
t.shape("wordlebox - Copy (2).gif")
t.goto(200,200)
t.done()


#6 2

#73 2