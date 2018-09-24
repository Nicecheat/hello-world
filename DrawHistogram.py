import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import GraphDict as GD

def draw(image):
	img=np.array(image)
	arr=img.flatten()
	n, bins, patches = plt.hist(arr, bins=256, normed=0, facecolor='black', alpha=0.75)
	plt.show()