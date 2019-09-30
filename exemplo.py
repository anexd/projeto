import cv2

imagemCarregada = cv2.imread("image.png",0)

cv2.imshow("ImagemCarregada",imagemCarregada)
cv2.imwrite("nova.png",imagemCarregada)
cv2.waitKey(0)
cv2.destroyAllWindows()
