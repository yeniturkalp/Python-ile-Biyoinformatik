# iki yöntem ile sözlük value değerlerine erişebiliriz

baz_sözlüğü = {
    
            "A": "Adenin",
            "T": "Timin",
            "G": "Guanin",
            "C": "Sitozin",
            "Baz sayısı:" : 4,
               }

print(baz_sözlüğü["A"]) # key değerini yazarak value değerini yazdırır

print("*** Get Metodu İle Erişim **")
x = baz_sözlüğü.get("T") #get metodu ile value değerine ulaşılır
print(x)

