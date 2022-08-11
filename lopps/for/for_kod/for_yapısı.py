baz_sözlüğü = ["Adenin","Timin","Guanin","Sitozin"]

print("*** FOR YAPISI ***")

for i in baz_sözlüğü:
    print(i) # listeyi elemanları teker teker gezerek hepsini yazdırır.
    
print("*** BREAK ***")

for i in baz_sözlüğü:
    print(i)
    if i == "Timin":
        break # Döngü timin elemanı okunana kadar devam eder timin elemanı okunduğu zaman döngü biter ve timin dahil o zaman kadar okunan elemanlar yazdırılır.
    # print(i) bu kodu da dahil edersek timin elemanı da yazdırılmaz
    
print("*** CONTIUNE ***")


for i in baz_sözlüğü:
    if i == "Timin":
        continue # Timin elemanı okunduğu zaman timini atlar ve diğer elemanları da okuyarak ekrana yazdırır. 
    print(i) #bu kodu da dahil edersek timin elemanı da yazdırılmaz
    
