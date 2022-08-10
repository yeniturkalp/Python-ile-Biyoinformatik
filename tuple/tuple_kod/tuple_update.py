# demet yapılarına append metodu ile ekleme veya değişikilk yapılamamaktadır fakat 2 yöntem ile demet yapısına öğe eklenebilir 

kodon = ('UAG', 'UUA', 'AGU', 'AGA', 'UCA', 'UUU', 'UCA', 'UUA')


# 1. yöntem: demet yapısını liste yapısına çevirerek ürün ekleme

print("***** 1.YÖNTEM *****")
y = list(kodon)
y[0] = "UGA" # index sıfır yerine UGA yazdırır
y.append("GUA") # GUA kodonunu ekler  
y.remove("AGU") #AGU öğesini siler
kodon = tuple(y)
print(kodon)
# 2. yöntem: demet yapısını demet yapısına ekleme
print("***** 2. YÖNTEM *****")
kodon2 = ("GGG","AUG")

kodon += kodon2 #kod2 demetini kodon demetine ekler

print(kodon)