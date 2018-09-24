import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import GraphDict


def H_E(image):
	Dict = GraphDict.dict(image)#调用GraphDict，建立图像字典，key是灰度值，value是图像中这一灰度值的像元的个数。
	rows,cols,dims = image.shape
	for row in range(0,rows):
		for col in range(0,cols):
			for j in range(0,3):
				i = round(image[row,col,j])#得到该点的灰度值并将其转换为0~255的量级
				sumDict = 0
				for x in range(0,i+1):
					sumDict = sumDict + Dict[x]
				image[row,col,j] = 255*sumDict/(rows*cols)#直方图均衡，并将灰度值转换回0~1量级
	
