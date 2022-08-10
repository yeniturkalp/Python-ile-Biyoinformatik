# iki yöntem ile sözlüğe öğe ekleyebiliriz

kodon = {
    
    "Stop Kod": "UAA",
    "Stop Kod2": "UAG",
    "Start Kod": "AUG"     
    }

print("BİRİNCİ İŞLEM")
kodon["Stop Kodon3"] = "UGA" # key = Stop kodon3, value= UGA olan bir öğe ekler
print(kodon)

print("İKİNCİ İŞLEM")
kodon.update({"Stop Kodon3": "UGA"})
print(kodon)