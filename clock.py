import time
import math
import random
import sys
t = time.localtime()
currentTime = time.strftime("%H:%M:%S", t)
intTime = currentTime.split(":")
for i in range(len(intTime)):
    intTime[i]= int(intTime[i])
nums =[]
for i in range(61):
    nums.append([])
    for j in range(i):
        nums[i].append([int(j), int(i)-int(j)])
index=random.randint(0,intTime[0]-1)
mindex=random.randint(0,intTime[1]-1)
print(nums[intTime[0]][index][0], "+", nums[intTime[0]][index][1], ":", nums[intTime[1]][mindex][0], "+", nums[intTime[1]][mindex][1])
#print(currentTime, end='\r')
while True:
    t = time.localtime()
    newTime = time.strftime("%H:%M:%S", t)
    intNewTime=newTime.split(":")
    for i in range(len(intNewTime)):
        intNewTime[i] =int(intNewTime[i])
    x=True
    for i in range(len(intNewTime)-1):
        if intNewTime[i] == intTime[i]:
            pass
        else:
            x=False
            intTime[i] = intNewTime[i]
    index=random.randint(0,intNewTime[0]-1)
    mindex=random.randint(0,intNewTime[1]-1)
    if x:
        pass
    else:
        print(nums[intNewTime[0]][index][0], "+", nums[intNewTime[0]][index][1], ":", nums[intNewTime[1]][mindex][0], "+", nums[intNewTime[1]][mindex][1])
