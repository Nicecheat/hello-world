import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

def dict(image):
	#为图像创建一个绘制直方图用的字典
	rows,cols,dims = image.shape
	Histo = {}
	for i in range(0,256):
		#建立一个空字典让其所有元素初值为0
		Histo[i] = 0
	for row in range(0,rows):
		for col in range(0,cols):
			j = round(image[row,col,0])
			#字典键值(该灰度值的像元数量)加一
			Histo[j] = Histo[j] + 1
	return Histo