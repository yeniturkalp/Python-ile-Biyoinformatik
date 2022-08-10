# birçok şekilde sözlük değerleri döngü ile yazdırılabilir

baz_sözlüğü = {
    
            "A": "Adenin",
            "T": "Timin",
            "G": "Guanin",
            "C": "Sitozin",
            "Baz sayısı:" : 4,
               }

for x in baz_sözlüğü:
    print(x) # key değerlerini yazdırır 


for x in baz_sözlüğü.keys():
    print(x) # key değerlerini yazdırır
    
print("********************************************************")

for x in baz_sözlüğü:
    print(baz_sözlüğü[x]) # key değerlerini yazdırır 
    
for x in baz_sözlüğü.values():
    print(x) # key değerlerini yazdırır
    
print("********************************************************")

for x,y in baz_sözlüğü.items():
    print(x,y)