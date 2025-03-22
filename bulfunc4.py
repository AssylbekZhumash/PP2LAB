import time
import math

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000.0)
    return math.sqrt(number)

number = 25100
milliseconds = 2123

result = delayed_sqrt(number, milliseconds)
print(f"Square root of {number} after {milliseconds} miliseconds is {result}")
