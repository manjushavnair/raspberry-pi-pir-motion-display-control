from gpiozero import MotionSensor
from signal import pause
from threading import Timer
from subprocess import run


pir = MotionSensor(4)
timer = None

def screenoff():
    print("screenoff")

def newTimer():
    print("newTimer")
    global timer
    timer = Timer(10.0, screenoff)
    timer.start()

def getScreenStatus():
    vcgencmdDisplayPower = run(['vcgencmd', 'display_power'], capture_output=True, text=True).stdout.strip()
    if (vcgencmdDisplayPower == "display_power=1"):
        return True
    else:
        return False

newTimer()

def screenOn():

    timer.cancel()
    newTimer()
    print("Motion, turning the screen on")
    print(getScreenStatus())

while True:
    pir.when_motion = screenOn
