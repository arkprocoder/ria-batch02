import math
import time

def circle(r):
    res=math.pi*r*r
    print("area of the circle ",res)
    time.sleep(5)
    return res

ReturnVal=circle(5) #ReturnVal=78.5398

print("return value is ",ReturnVal)