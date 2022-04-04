from PIL import Image
import numpy as np
soonToSus = Image.open('notSus.png')

x = int(soonToSus.size[0]/5)
y = int(soonToSus.size[1]/5)

print(x,y)

soonToSus.show()

sus = np.array(soonToSus.convert("L"))

susArray = np.array([[0,100,100,100,0],[100,100,200,200,0],[100,100,100,100,0],[0,100,0,100,0]])

susMap = np.empty((x*5,y*5))
print(susMap.shape)

susMap[0] = np.tile(susArray[0],x)
susMap[1] = np.tile(susArray[1],x)
susMap[2] = np.tile(susArray[2],x)
susMap[3] = np.tile(susArray[3],x)

print(susArray)

print(susMap)

Image.fromarray(susMap).show()