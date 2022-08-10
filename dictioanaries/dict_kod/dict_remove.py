# birkaç yöntem ile öğeler silinir

baz_sözlüğü = {
    
            "A": "Adenin",
            "T": "Timin",
            "G": "Guanin",
            "C": "Sitozin",
            "Baz sayısı:" : 4,
               }
print(" *** POP ***")
baz_sözlüğü.pop("A") # Adenin, key: value değerlerini siler
print(baz_sözlüğü)

print(" *** POP ITEM ***")
baz_sözlüğü.popitem() # en son öğeyi silet yani baz sayı, key:value değerini siler 
print(baz_sözlüğü)

print(" *** DEL ***")
del baz_sözlüğü["G"] # Guanini siler. Eğer del baz_sözlüğü şeklinde yazsaydık sözlük yapısını tamamen silerdi  
print(baz_sözlüğü)

print(" *** CLEAR ***")
baz_sözlüğü.clear() # Sözlük yapısının içerisini siler boş bir sözlük yapısı geriye döner
print(baz_sözlüğü)
