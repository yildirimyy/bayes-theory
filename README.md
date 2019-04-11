# Bayes Teorisi

* İngiliz matematikçi Thomas Bayes'ten adını alan Bayes Teorisi sonucun sebebini bulurken bu sonucun hangi olasılıkla ve hangi sebeplerden kaynaklandığını bulmaya yarar.
* Makine Öğrenmesi gibi bir çok alanda sık sık bu popüler olasılık hesabı kullanılır.

- - -

![](https://raw.githubusercontent.com/yildirimyy/bayes-theory/master/Screen/1.png) 

- - -

## SORU: Bir araştırmaya göre her 43 çocuktan 1 tanesi, yetişkinlikte ortaya çıkan belli bir hastalığa yakalanmakta ve tam güvenilir olmamasına rağmen yapılan test sonuçlarına göre, hastalıklı bir çocuğun testi %80 pozitif, sağlıklı bir çocuğun testi ise %10 pozitif sonuç vermektedir. Bu bilgilere göre test sonucu pozitif olan bir çocuğun gerçekten hasta olma olasılığı nedir?

## ÇÖZÜM: 

P(A) = Çocuğun hasta olma olasılığı = 1/43
P(B) = Testin pozitif çıkma olasılığı = (1/43) * (0.80) + (42/43) * (0.10) = 5/43
P(A|B) = Pozitif çıkan testin hastalık çıkma olasığılı (soru)
P(B|A) = Hastalıklı çocucuğun testinin pozitif çıkma olasılığı = 0.80

P(A|B) = P(B|A) * P(A)/P(B) = (0.80*1/43) / (5/43) = 0.16 = %16

- - -
![](https://raw.githubusercontent.com/yildirimyy/bayes-theory/master/Screen/2.png) 

- - -

![](https://raw.githubusercontent.com/yildirimyy/bayes-theory/master/Screen/3.png) 

- - -

## SORU: Bir alerji testinin her zaman doğru sonuç vermediği biliniyor. Gerçekten alerjisi olan insanlar için testin "Evet" sonucu vermesi %80 oranındadır. Alerjisi olmayan insanlar için testin "Evet" sonucu vermesi de %10 oranındadır. Nüfusun %1'inde alerji varsa ve test "Evet" çıkıyorsa kaşınan birinin gerçekten alerji olma olasılığı nedir?

## ÇÖZÜM: 

A: Alerji, B: Testin "Evet" çıkması

P(A) = Alerji olasılığı = 0.01
P(B) = Testin "Evet" çıkma olasılığı (hesapllanması gerek)
P(A|B) = Testin "Evet" çıkması durumunda alerji olasılığı (soru)
P(B|A) = Alerji olması durumunda testin evet çıkma olasılığı = 0.80

P(B) = 0.01 * 0.80 + 0.99 * 0.10 = 0.107

P(A|B) = P(A) * P(B|A)/P(B) = (0.01 * 0.80) / 0.107 = 0.075 = %7

- - - 

![](https://raw.githubusercontent.com/yildirimyy/bayes-theory/master/Screen/4.png) 

- - -

* https://medium.com/@enginunal/bayes-teoremi-431543ad9a59
* http://www.datascience.istanbul/2017/06/29/bayes-teoremi-giris/

# bayes-theory