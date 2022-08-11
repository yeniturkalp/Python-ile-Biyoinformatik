# Bir kod kümesinde belirli sayıda döngü yapmak için range() işlevini kullanabiliriz,
# range() işlevi , varsayılan olarak 0'dan başlayan ve 1 (varsayılan olarak) artan bir sayı dizisi döndürür ve belirtilen bir sayıda biter.

print("*** İŞLEM 1 ***")
for x in range(6):
  print(x) # 0'dan başlar 5'e kadar(dahil) değerleri yazdırır.
print("*** İŞLEM 2 ***") 
for x in range(2, 6):
  print(x) #♣ 2'den başlar 5'e kadar (dahil) değerleri yazdırır
print("*** İŞLEM 3 ***")
for x in range(2, 10, 2):
  print(x) # 2'den başlar 9'a kadar(8 sayısı dahil olur) ikişer ikişer artarak değerleri yazdırır 