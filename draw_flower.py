from turtle import *
#renkler sistemden çekildi colorsys aracılığı ile
import colorsys
#hız belirlendi 0'a yaklaştıkça hız artıyor
speed(0.5)
#Çizim kalınlığı belirlendi
pensize(3)
#Arkaplan rengi belirlendi
bgcolor("black")
#renk skalasının başlama noktası belirlendi
hue = 0.0
#çizim döngüye alındı
for x in range(300):
#rgb tonları ayarlandı
    col = colorsys.hsv_to_rgb(hue,1,1)
#belirlenen renk ile çizim gerçekleştiirldi
    pencolor(col)
#rengin ne kadar zamanda değişeceği belirlendi
    hue += 0.005
#çizimin başlangıç noktası ve çizim açısı belirlendi
    circle(5-x, 100)
#yapraklar arası açı belirlendi
    lt(80)
#çizimin başlangıç noktası ve çizim açısı belirlendi
    circle(5-x, 100)
#Çizimin merkezde kalması sağlandı
    rt(100)