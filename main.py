# TODO Make the thing a little better looking by using the blend method

from PIL import Image
import numpy as np
from PIL import ImageOps
soonToSus = Image.open('notSus.png')

## How Sus do you want it
deltaSus = 8

x = int(soonToSus.size[0]/5)
y = int(soonToSus.size[1]/5)

## PreSus
soonToSus.show()

## B&W Sus
susBW = np.array(soonToSus.convert("L"))
print(np.shape(soonToSus))

## Color Sus
susR, susG, susB = soonToSus.split()
susR = np.array(susR.convert())
susG = np.array(susG.convert())
susB = np.array(susB.convert())

r,g,b = soonToSus.split()

## This Array is pretty sus
susArray = np.multiply(np.array([[1,2,2,2,1],[2,2,3,3,1],[2,2,2,2,1],[1,2,1,2,1],[1,1,1,1,1]]),deltaSus)

susMap = np.empty((x*5,y*5))
print(susMap.shape)

susMap = np.tile(susArray,(x,y))
## Find the darkness of parts of the picture to be changed to something more sus
HowSusCanWeSus = np.subtract(susMap,susBW)

# Image.fromarray(HowSusCanWeSus).show()

susR = HowSusCanWeSus * susR
susG = HowSusCanWeSus * susG
susB = HowSusCanWeSus * susB
# Image.fromarray(susR).show()
# Image.fromarray(susG).show()
# Image.fromarray(susB).show()

# susR = Image.fromarray(susR)
# susG = Image.fromarray(susG)
# susB = Image.fromarray(susB)
# ImageOps.fit(susR,soonToSus.size)
print(np.max(susR), np.min(susR))
test = np.append(np.append(susR,susG),susB)

test = np.reshape(test,(x*5,y*5,3),'F')
print(np.shape(test))
print(np.max(susR),np.min(susR))
for i in range(0, x*5):
    for ii in range(0, y*5):
        for iii in range(0, 3):
            test[i][ii][iii] = abs(test[i][ii][iii])/256

test = Image.fromarray(test.astype(np.uint8))
print(test)
test = ImageOps.mirror(test.rotate(-90))
test.show()
test.save("sus.png")
# print(test)


