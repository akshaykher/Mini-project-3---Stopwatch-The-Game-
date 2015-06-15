# template for "Stopwatch: The Game"
import simplegui

# define global variables
tenth_of_second = 0
correct_stop = 0
total_stop = 0
Value_Tenth = 0
timer_is_running = False

##define helper functions

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    # t is less than 1s
    global Value_Tenth
    if(t<10):
        A=0
        B=0
        C=0
        D=t%10
        Value_Tenth = D
        return str(A)+":"+str(B)+str(C)+"."+str(D)
    # t is between 1s-10s
    elif(t>=10 and t<100):
        A=0
        B=0
        C=t//10
        D=t%10
        Value_Tenth = D
        return str(A)+":"+str(B)+str(C)+"."+str(D)
    # t is between 10s-60s
    elif(t>=100 and t<600):
        A=0
        B=t//100
        C=(t%100-t%10)/10
        D=t%10
        Value_Tenth = D
        return str(A)+":"+str(B)+str(C)+"."+str(D)
    # t is more than 60s
    else:
        A=int(t/600)
        X=t-A*600
        # t is less than 1s
        if(X<10):
            B=0
            C=0
            D=X%10
        # t is between 1s-10s
        elif(X>=10 and X<100):
            B=0
            C=X//10
            D=X%10
        # t is between 10s-60s
        else:
            B=X//100
            C=(X%100-X%10)/10
            D=X%10
        # t is more than 60s
    Value_Tenth = D
    return str(A)+":"+str(B)+str(C)+"."+str(D)

##define event handlers
    
# define event handler for timer with 0.1 sec interval
def tick() :
    """
    This integer will keep track of the time in tenths of seconds.
    """
    global tenth_of_second
    tenth_of_second +=1
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_is_running
    if(timer_is_running == False):
        MyTimer.start()
        timer_is_running = True
         
def stop():
    global total_stop
    global timer_is_running
    global Value_Tenth
    global correct_stop
    
    if(timer_is_running == True and Value_Tenth==0):
        correct_stop = correct_stop +1
        total_stop = total_stop +1
        MyTimer.stop()
    if(timer_is_running == True and Value_Tenth !=0):
        total_stop = total_stop +1
        MyTimer.stop()
    timer_is_running = False
        
def reset():
    global tenth_of_second
    global total_stop
    global correct_stop
    MyTimer.stop()
    tenth_of_second = 0
    total_stop = 0
    correct_stop = 0

# define draw handler
def draw(canvas) :
    global tenth_of_second
    global correct_stop
    global total_stop
    canvas.draw_text(format(tenth_of_second), (100,150), 36, "Red")
    canvas.draw_text(str(correct_stop),(220,35),36,"Green")
    canvas.draw_text("/",(240,45),70,"Green")
    canvas.draw_text(str(total_stop),(260,35),36,"Green")

# create frame
MyFrame = simplegui.create_frame("StopWatch", 300, 300)

# register event handlers
MyTimer = simplegui.create_timer(100, tick)
MyFrame.set_draw_handler(draw)
MyStopButton = MyFrame.add_button("Start",start,150)
MyStartButton = MyFrame.add_button("Stop",stop,150)
MyResetButton = MyFrame.add_button("Reset",reset,150)

# start frame
MyFrame.start()
MyTimer.stop()

# Please remember to review the grading rubric
