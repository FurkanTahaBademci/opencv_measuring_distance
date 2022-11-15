import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input', help='İnput İmage Path', required=True)
parser.add_argument('-o','--output', help='Output İmage Path', required=False)
args = vars(parser.parse_args())



font = cv2.FONT_HERSHEY_COMPLEX  

img = cv2.imread(args['input'])   
image_norm = cv2.normalize(img, None, alpha=0,beta=200, norm_type=cv2.NORM_MINMAX)
gray = cv2.cvtColor(image_norm,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
dilate = cv2.dilate(blur,None,iterations=3)
otsu = cv2.threshold(dilate,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
conturs,_ = cv2.findContours(otsu,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

gecis_kontrol = 0

for c in conturs:
    area = cv2.contourArea(c)
    x,y,w,h = cv2.boundingRect(c)
    test = w/h

    epsilon = 0.01*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)

    if area > 100:

        if area > 100 and 1.10 > test > 0.90 and len(approx) == 4:

            x = approx.ravel()[0]    
            y = approx.ravel()[1] 
            
            cv2.putText(img,"DETECT",(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0))
            referans_uzunluk = w
            gecis_kontrol = 1
            break 


if gecis_kontrol==1:

    for c in conturs:

        area = cv2.contourArea(c)

        if area > 100:
                
            epsilon = 0.01*cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)

            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

            """
            x = approx.ravel()[0]    
            y = approx.ravel()[1]
            w = approx.ravel()[2]
            h = approx.ravel()[3]
            """
            
            cv2.circle(img,(x,y),5,(0,0,255),-1)
            cv2.circle(img,(x+w,y),5,(0,0,255),-1)
            cv2.circle(img,(x,y+h),5,(0,0,255),-1)
            cv2.circle(img,(x+w,y+h),5,(0,0,255),-1)

            en_gercek_uzunluk = int(30 * w) // referans_uzunluk
            boy_gercek_uzunluk = int(30* h) // referans_uzunluk


            cv2.putText(img, (str(boy_gercek_uzunluk)+" mm"),(x,y+h//2),font,0.5,(0,255,0))
            cv2.putText(img, (str(en_gercek_uzunluk)+" mm"),(x+w//2,y),font,0.5,(0,255,0))
            
            
            print("x: ",x," y: ",y, " w: ",w," h: ",h)


cv2.imshow("img",img)
print("Referans Uzunluk: ",referans_uzunluk)    
cv2.waitKey(0)
cv2.imwrite(args['output'])
cv2.destroyAllWindows()

    