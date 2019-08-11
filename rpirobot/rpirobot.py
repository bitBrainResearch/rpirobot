from gpiozero import LED

# 11, 12
# 13, 15
rightForward = LED(17)
rightBackward = LED(18)
leftForward = LED(27)
leftBackward = LED(22)

def forward():
    clear()
    rightForward.on()
    leftForward.on()

def backward():
    clear()
    rightBackward.on()
    leftBackward.on()

def left():
    clear()
    rightForward.on()
    leftBackward.on()

def right():
    clear()
    rightBackward.on()
    leftForward.on()
    
def clear():
    rightBackward.off()
    rightForward.off()
    leftBackward.off()
    leftForward.off()