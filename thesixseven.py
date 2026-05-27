import sys
import time

print("Welcome to Grade 1 Math")

while True:
    sixseven = int(input("What is 6+7 = "))

    #Wrong Answer
    if sixseven == 13:
        print("wrong answer!")
    else:
        break

while True:
    print("67", end=" ")
    sys.stdout.flush()
    time.sleep(0.2)