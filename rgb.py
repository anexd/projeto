import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("brasao.jpg")
color = ('b','g','r')

for i, col in enumerate (color):
    print (i,col)
