# liste elemanlarına erişim birçok yöntem ile yapılmaktadır.



kodon = ["UAG","AGU", "AGA"]

print("********** İNDEKSLEME **********")
# index numarası ile elemanı okuma 
print(kodon[1])# index numarası 1 olanı yazdırır yani AGU kodonu yazılır.


print("********** NEGATİF İNDEKSLEME **********")
# negatif indexleme ile elemanı okuma 
print(kodon[-1])# index numarası -1 olanı yazdırır yani AGA kodonu yazılır.


print("********** DİZİN ARALIĞI **********")
# dizin aralığı ile elemanları okutma 
print(kodon[0:2]) # 0 indexten başlar 2.indexe kadar(dahi değil) olan elemanları yazdırır. UAG ve AGU yazılır


print("********** ELEMAN SORGULAMA **********")
# liste içinde elemanın varlığını sorgulama 
if "UAG" in kodon:
    print("Bu liste yapısında durdurma kodonu:" + kodon[0] + " " + "bulunmaktadır") 


