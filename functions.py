# HW: N
# Name: Hani Almansouri
# ID: 123456789
#
# -------------------------------------------------

import turtle as t

r = t.Turtle()
r.color('red')
r.hideturtle()
r.pensize(4)
w = r.getpen()

a = 0
b = 0
x_index = 0
y_index = 0


def mark(x, y):  # This function is called when the left mouse button is clicked the input argument x and y are the
    # screen coordinate.
    t.pencolor('red')

    def main():
        if not check_location(x_index, y_index):
            t.goto(x, y)
            t.penup()

        elif check_location(x_index, y_index):
            if shared_variables.x_is_playing:
                draw_cross(a, b)
                assign_avariables(x_index, y_index, 0)
                print_winner()
                shared_variables.x_is_playing = False
            elif not shared_variables.x_is_playing:
                draw_circle(a, b)
                assign_avariables(x_index, y_index, 1)
                print_winner()
                shared_variables.x_is_playing = True

    def boxes(x=x, y=y):
        global a
        global b
        global x_index
        global y_index

        if -150 <= x <= -50 and 50 <= y <= 100:  # x=0
            # This is x00
            a = -150
            b = 100
            x_index = 0
            y_index = 0
            main()
        if -50 <= x <= 50 and 50 <= y <= 100:
            # This is x01
            a = -50
            b = 100
            x_index = 0
            y_index = 1
            main()
        if 50 <= x <= 100 and 50 <= y <= 100:
            # This is x02
            a = 50
            b = 100
            x_index = 0
            y_index = 2
            main()

        if -150 <= x <= -50 and -50 <= y <= 50:  # x = 1
            # This is x10
            a = -150
            b = 0
            x_index = 1
            y_index = 0
            main()
        if -50 <= x <= 50 and -50 <= y <= 50:
            # This is x11
            a = -50
            b = 0
            x_index = 1
            y_index = 1
            main()
        if 50 <= x <= 100 and -50 <= y <= 50:
            # This is x12
            a = 50
            b = 0
            x_index = 1
            y_index = 2
            main()

        if -150 <= x <= -50 and -150 <= y <= -50:  # x  = 2
            # This is x20
            a = -150
            b = -100
            x_index = 2
            y_index = 0
            main()
        if -50 <= x <= 50 and -150 <= y <= -50:
            # This is x21
            a = -50
            b = -100
            x_index = 2
            y_index = 1
            main()
        if 50 <= x <= 100 and -150 <= y <= -50:
            # This is x22
            a = 50
            b = -100
            x_index = 2
            y_index = 2
            main()

    def draw_circle(a, b):
        t.penup()
        t.goto(a + 50, b - 40)
        t.setheading(0)
        t.pendown()
        t.circle(40)
        t.penup()

    def draw_cross(a, b):
        t.penup()
        t.goto(a + 20, b + 30)
        t.setheading(-45)
        t.pendown()
        t.forward(85)
        t.penup()
        t.goto(a + 80, b + 30)
        t.setheading(-135)
        t.pendown()
        t.forward(85)
        t.penup()

    def print_winner():
        if check_status() == 0:
            shared_variables.flag_status = False
            if not shared_variables.flag_status:
                t.penup()
                t.goto(-150, 150)
                t.write("X Wins!")
        elif check_status() == 1:
            shared_variables.flag_status = False
            if not shared_variables.flag_status:
                t.penup()
                t.goto(-150, 150)
                t.write("0 Wins!")
        elif shared_variables.x00 == shared_variables.x01 == shared_variables.x02 == shared_variables.x10 ==\
                shared_variables.x11 == shared_variables.x12 == shared_variables.x20 == shared_variables.x21 ==\
                shared_variables.x22 is not None and check_status() != 1\
                or \
                shared_variables.x00 == shared_variables.x01 == shared_variables.x02 == shared_variables.x10 == \
                shared_variables.x11 == shared_variables.x12 == shared_variables.x20 == shared_variables.x21 == \
                shared_variables.x22 is not None and check_status() != 0:
                    shared_variables.flag_status = False

    if x < - 150 or x > 150 or y < -150 or y > 150:
        global a
        global b
        global x_index
        global y_index
        w.penup()
        w.goto(-150, 150)
        w.write("You clicked outside the grid")
    else:
        w.clear()
        if shared_variables.flag_status:
            boxes()


# ------------------------------------------------------------------------------------------------
# do not change the code below
def reset(x, y):  # resets when right mouse button is clicked
    t.reset()
    t.delay(0)
    t.hideturtle()
    draw_grid()
    t.pensize(5)
    shared_variables.x00 = None
    shared_variables.x01 = None
    shared_variables.x02 = None
    shared_variables.x10 = None
    shared_variables.x11 = None
    shared_variables.x12 = None
    shared_variables.x20 = None
    shared_variables.x21 = None
    shared_variables.x22 = None
    
    shared_variables.x_is_playing = True
    shared_variables.flag_status = True


def draw_grid():   # Draws the grid. The width and hight of each square is 100. The first vertical line from the left
    # starts at -150. the first horizontal line from the bottom starts at -150
    for i in range(4):
        t.penup()
        t.goto(-150+100*i, 150)
        t.pendown()
        t.goto(-150+100*i, -150)
    for i in range(4):
        t.penup()
        t.goto(-150, 150-100*i)
        t.pendown()
        t.goto(150, 150-100*i)


class shared_variables:  # is a class. you did not take this yet, but we will use it anyway. The variable in the class
    # will be used as a global variable so we can store values to them and use them between functions.
    x00 = None      # grid variables to store 0 for X or 1 for O for each position.
    x01 = None      # x02 | x12 | x22
    x02 = None      # ----------------
    x10 = None      # x01 | x11 | x21
    x11 = None      # ----------------
    x12 = None      # x00 | x10 | x20
    x20 = None
    x21 = None
    x22 = None
    x_is_playing = True     # True if it is X's turn. Flase if it O's turn
    flag_status = True      # True if the game is still going. Flase if the game is finished.
    
    
def assign_avariables(x,y,value):   # gives the grid variable 0 for X or 1 for O. make sure that the input arguments
    # x and y are either 0, 1, or 2.
    if x == 0 and y == 0:
        shared_variables.x00 = value
    elif x == 0 and y == 1:
        shared_variables.x01 = value
    elif x == 0 and y == 2:
        shared_variables.x02 = value
    elif x == 1 and y == 0:
        shared_variables.x10 = value
    elif x == 1 and y == 1:
        shared_variables.x11 = value
    elif x == 1 and y == 2:
        shared_variables.x12 = value
    elif x == 2 and y == 0:
        shared_variables.x20 = value
    elif x == 2 and y == 1:
        shared_variables.x21 = value
    elif x == 2 and y == 2:
        shared_variables.x22 = value


def check_location(x, y):      # checks if the location is empty (True) or used before (False). Make sure that the
    # input arguments x and y are either 0, 1, or 2.
    if x == 0 and y == 0 and shared_variables.x00 != None:
        return False
    elif x == 0 and y == 1 and shared_variables.x01 != None:
        return False
    elif x == 0 and y == 2 and shared_variables.x02 != None:
        return False
    elif x == 1 and y == 0 and shared_variables.x10 != None:
        return False
    elif x == 1 and y == 1 and shared_variables.x11 != None:
        return False
    elif x == 1 and y == 2 and shared_variables.x12 != None:
        return False
    elif x == 2 and y == 0 and shared_variables.x20 != None:
        return False
    elif x == 2 and y == 1 and shared_variables.x21 != None:
        return False     
    elif x == 2 and y == 2 and shared_variables.x22 != None:
        return False     
    else:
        return True
        
def check_status(): #checks if the game is still running (returns None) or if it is finished (returns 0 for X or 1 for O).
    if shared_variables.x00 ==  shared_variables.x11 == shared_variables.x22 != None:       #x00
        return shared_variables.x00
    elif shared_variables.x00 == shared_variables.x10 == shared_variables.x20 != None:
        return shared_variables.x00
    elif shared_variables.x00 == shared_variables.x01 == shared_variables.x02 != None:
        return shared_variables.x00
        
    elif shared_variables.x01 == shared_variables.x11 == shared_variables.x21 != None:     #x01
        return shared_variables.x01
        
    elif shared_variables.x02 == shared_variables.x12 == shared_variables.x22 != None:     #x02
        return shared_variables.x02
    elif shared_variables.x02 == shared_variables.x11 == shared_variables.x20 != None:
        return shared_variables.x02
    
    elif shared_variables.x10 == shared_variables.x11 == shared_variables.x12 != None:     #x10
        return shared_variables.x10
        
    elif shared_variables.x22 == shared_variables.x21 == shared_variables.x20 != None:     #x22
        return shared_variables.x22
    else:
        return None
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
