
# Görüntü İşleme Teknikleri Kullanarak Mesafe Ölçümü 

Görüntü üzerindeki herhangi bir nesneyi referans alarak görüntü üzerindeki tüm kontürleri milimetre hassisiyetinde ölçebilirsiniz. Bu çalışmada 3x3 cm ebatlarında siyah kare bir nesne referans alınmıştır. 

    
## Eklenmesi Planlanan özellikler
Siyah nesne yerine daha benzersiz olan QR kod referans alınarak doğruluk daha da arttırılacaktır.

## Kodu Çalıştırmak için
### Fotoğraf 
```
python image_measuring_distance.py -i <input_image_path> -o <output_image_path>
```
### Video 
#### Video üzerinden kullanım da IP kamera kullanmak isterseniz video_measuring distance.py içerisinde kullanabileceğiniz yorum satırları bulunmaktadır 

```
python video_measuring distance.py
```
# Örnekler
<br>

![{ width: 200px; }](https://raw.githubusercontent.com/furkantahabademci/opencv_measuring_distance/main/images/input_images/input_1.jpg)

![{ width: 200px; }](https://raw.githubusercontent.com/furkantahabademci/opencv_measuring_distance/main/images/output_images/output_1.jpg)

<br>

![{ width: 200px; }](https://raw.githubusercontent.com/furkantahabademci/opencv_measuring_distance/main/images/input_images/input_2.jpg)

![{ width: 200px; }](https://raw.githubusercontent.com/furkantahabademci/opencv_measuring_distance/main/images/output_images/output_2.jpg)

<br>

![{ width: 200px; }](https://raw.githubusercontent.com/furkantahabademci/opencv_measuring_distance/main/images/input_images/input_3.jpg)

![{ width: 200px; }](https://raw.githubusercontent.com/furkantahabademci/opencv_measuring_distance/main/images/output_images/output_3.jpg)