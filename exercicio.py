import cv2
import numpy as np
 
img = cv2.imread('pout.jpg') # lendo a imagem
img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
 
cv2.imwrite('result.jpg',hist_equalization_result) # gerando outra imagem
imagemCarregada = cv2.imread("result.jpg",0)

cv2.imshow("ImagemCarregada",imagemCarregada)# mostrar imagem


brasao = imagemCarregada[570:750,430:600] #fatia da imagem
cv2.imwrite("brasao.jpg",brasao)






cv2.waitKey(0) #pause na tela
cv2.destroyAllWindows()