import time

seconds = 5

def countdown(seconds):
    while seconds > 0:
        print(seconds, "Mississippi")
        time.sleep(1)
        seconds -= 1
    print("Ready or not, here I come!")

countdown(seconds)

# Drive code

# No tests for this lab