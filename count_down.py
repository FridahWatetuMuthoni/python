import time
# range(start: stop: step)-> a negative step means that its counting down
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)

print("Happy New Year")
