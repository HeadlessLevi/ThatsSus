from PIL import Image
import numpy as np
from PIL import ImageOps
soonToSus = Image.open('notSus.png')

## How Sus do you want it
deltaSus = 10

x = int(soonToSus.size[0]/5)
y = int(soonToSus.size[1]/5)

## PreSus
soonToSus.show()

## B&W Sus
susBW = np.array(soonToSus.convert("L"))

## Color Sus
susR = np.empty([x,y],np.uint8)
susR, susG, susB = Image.Image.split(soonToSus)
r,g,b = soonToSus.split()

## This Array is pretty sus
susArray = np.multiply(np.array([[0,1,1,1,0],[1,1,2,2,0],[1,1,1,1,0],[0,1,0,1,0],[0,0,0,0,0]]),deltaSus)

susMap = np.empty((x*5,y*5))
print(susMap.shape)

susMap = np.tile(susArray,(x,y))
## Find the darkness of parts of the picture to be changed to something more sus
HowSusCanWeSus = np.subtract(susMap,susBW)

# Image.fromarray(HowSusCanWeSus).show()

susR = np.subtract(HowSusCanWeSus,susR)
susG = np.subtract(HowSusCanWeSus,susG)
susB = np.subtract(HowSusCanWeSus,susB)
# Image.fromarray(susR).show()
# Image.fromarray(susG).show()
# Image.fromarray(susB).show()

# susR = Image.fromarray(susR)
# susG = Image.fromarray(susG)
# susB = Image.fromarray(susB)

sus = Image.merge("RGB",(r,g,b))
sus.show()
