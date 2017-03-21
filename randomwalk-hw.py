import math
import random
import matplotlib.pyplot as plt
import numpy as np


class Agent:
    """The following class determines how far an agent walks for a certain number of steps """
    def __init__(self):
        '''Initization method'''
        self.x = 0.0
        self.y = 0.0
        self.d = random.random()*2*math.pi
        self.v = 1.0
    def step(self):
        '''This method is what moves the agent around'''
        self.shift_direction()
        self.x +=  self.v * math.cos(self.d)
        self.y +=  self.v * math.sin(self.d)

    def step2(self):
        self.d = self.d + np.random.normal(0,1) # velocity
        self.x += self.v* math.cos(self.d)
        self.y += self.v * math.sin(self.d)
    def shift_direction(self):
        self.d = random.random() * 2 * math.pi


# Randomness

a = Agent()
time = 0
xhis = []
yhis = []
while time < 100:
    a.step()
    xhis.append(a.x)
    yhis.append(a.y)
    a.step()
    time += 1
plt.xlabel('Position')
plt.ylabel('Direction')
plt.title('Random Walk')
plt.plot(xhis, yhis)
plt.show()

# Distance
i = 0
dist =[]
while i < 100:
    length = math.sqrt(((xhis[i]**2))+ (yhis[i]**2))
    dist.append(length)
    i+=1
somenum = 0
e = []
while somenum < 100:
    e.append(somenum)
    somenum +=1
plt.plot(e,dist)
plt.xlabel('Position')
plt.ylabel('Direction')
plt.title('Random Walk')
plt.show()

# part 2

# Randomness

a = Agent()
time = 0
xhis = []
yhis = []
while time < 100:
    xhis.append(a.x)
    yhis.append(a.y)
    a.step2()
    time += 1
plt.xlabel('Position')
plt.ylabel('Direction')
plt.title('Random Walk')
plt.plot(xhis, yhis)
plt.show()

# Distance
i = 0
dist =[]
while i < 100:
    length = math.sqrt(((xhis[i]**2))+ (yhis[i]**2))
    dist.append(length)
    i+=1
somenum = 0
e = []
while somenum < 100:
    e.append(somenum)
    somenum += 1
plt.plot(e,dist)
plt.xlabel('Position')
plt.ylabel('Direction')
plt.title('Random Walk')
plt.show()
