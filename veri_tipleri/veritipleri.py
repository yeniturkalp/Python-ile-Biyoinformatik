#Veri Tipini Belirterek Değişken Oluşturma

a = 5      #Sayısal tip olan (int)
b = "5"    #Metin tipi olan (str)

print(type(a))    # <class 'int'>
print(type(b))    # <class 'str'>

#NOT: type() kodu içerisine yazılan kodun hangi veri olduğunu söyler.


#Veri Tipleri Arası Dönüşüm

a = 5

print(a)          # 5
print(type(a))    # <class 'int'>

a = float(a)

print(a)          # 5.0
print(type(a))    # <class 'float'>


#PYTHON SAYILAR

a = 5        # int
b = 46.53    # float
c = 3j        # complex

print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>

#Int Veri Tipi


#Bir int değişken sonsuz uzunlukta pozitif ve negatif tam sayılardan oluşabilir. Sadece ondalık değerlere sahip olamaz.

x = 10
y = 35656222554887711
z = -3255522

print(type(x))    # <class 'int'>
print(type(y))    # <class 'int'>
print(type(z))    # <class 'int'>


# Float Veri Tipi

#Bir float değişken bir veya daha fazla uzunluktaki küsüratlı basamağa sahip pozitif ve negatif sayılardan oluşabilir.


x = 1.10
y = 1.0
z = -35.59985

print(type(x))    # <class 'float'>
print(type(y))    # <class 'float'>
print(type(z))    # <class 'float'>


#Complex Veri Tipi

#Bir complex  veri tipinde sanal kısımlar j harfiyle belirtilir.



#Rastgele Sayı Üretme & Oluşturma


import random

print(random.randrange(1,10)) # 1 ile 9 arasında sayı üretir.


#Matematiksel İşlemler ve Fonksiyonlar

# # Toplama İşlemi
# >>> x + y

# # Çıkarma İşlemi
# >>> x - y

# # Çarpma İşlemi
# >>> x * y    

# # Bölme İşlemi
# >>> x / y

# # Bölme İşlemi (Küsüratı siler)
# >>> x // y

# # Mod İşlemi
# >>> x % y

# # Sayıyı negatife çevirme
# >>> -x

# # Mutlak Değer
# >>> abs(x)

# # Kompleks Sayının Eşleniği
# >>> c.conjugate()

# # Bölme ve Mod İşlemi (x // y, x % y)
# >>> divmod(x, y)

# # X in Y üssü (ikiside aynı işlemi yapar)
# >>> pow(x, y)
# >>> x**y

