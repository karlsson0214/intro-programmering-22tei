import random
import os
import time

runners = []

for i in range(8):
    runners.append(0)

# runners = [1, 3, 2, 1, 1, 3, 3, 2]

def draw(runners):
    for runner in runners:
        text = ' ' * runner + 'X'
        print(text)
    print()

for i in range(10):
    for j in range(len(runners)):
        runners[j] += random.randint(1, 3)
    os.system('cls')
    draw(runners)
    time.sleep(0.5)