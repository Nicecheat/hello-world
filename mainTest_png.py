import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as img
import numpy as np
import GraphDict as GD
import HistogramEqualization as HE
import DrawHistogram as DH

test = np.array(Image.open('test.png'))

HE.H_E(test)#直方图均衡

Dict = GD.dict(test)
print(Dict)#打印像素字典

DH.draw(test)#描绘直方图

plt.imshow(test)
plt.axis('off')
plt.show()

