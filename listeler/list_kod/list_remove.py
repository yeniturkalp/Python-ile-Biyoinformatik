# liste elemanları birkaç yöntem ile silinebilir

kodon = ['UAG', 'UUA', 'AGU', 'AGA', 'UCA', 'UUU', 'UCA', 'UUA']

# pop yöntemi: belirtilen elemanı siler eğer index no belirtilmez ise son eleman silinir.

print("***** POP YÖNTEMİ *****")
kodon.pop(2) # index 2yi siler
print(kodon)

# del metodu: belirtilen öğeyi siler ancak index no girilmez ise liste yapısını tamamen siler.
print("***** DEL YÖNTEMİ *****")
del kodon[1] # index 1i siler
print(kodon)

# clear yöntemi:liste yapısının içerisini tamamen temizler
print("***** CLEAR YÖNTEMİ *****")
kodon.clear() # index 0ı siler  
print(kodon)