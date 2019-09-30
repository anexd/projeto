import numpy as np
import cv2
  
 
# reads an input image 
img = cv2.imread('animal.jpg',1) 

print(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('original', img)
cv2.imshow('cinza', gray)

print ("Altura (height): %d pixels" % (img.shape[0]))
print ("Largura (width): %d pixels" % (img.shape[1]))
print ("Canais (channels): %d"      % (img.shape[2]))


#pegando a cor de um pixel
(b, g, r) = img[0, 0]
print ("Cor do pixel em (0, 0) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))

(b, g, r) = img[305, 250]
print ("Cor do pixel em (250, 305) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))

(b, g, r) = img[30, 250]
print ("Cor do pixel em (250, 30) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))


#mudando a cor de um pixel
img2 = img
img2[0, 0] = (100, 10, 10)
img2[10:50, 10:50] = (100, 10, 10)
cv2.imshow("Modificada.jpg", img2)

#fatiando uma imagem

fatia = img[0:150, 150:300]
cv2.imshow("Fatia da imagem", fatia)

cv2.imwrite("nova.png", fatia)    


cv2.waitKey(0)
