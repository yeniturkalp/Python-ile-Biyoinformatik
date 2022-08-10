# 2 şekilde ekleme işlemi yapılır

kodon = {
    
    "Stop Kod": "UAA",
    "Stop Kod2": "UAG",
    "Start Kod": "AUG"     
    }
print(" BİRİNCİ İŞLEM ")
kodon["Stop Kod"] = "UGA" #UAA yerine UGA kodonu yazılır
print(kodon)

print(" İKİNCİ İŞLEM ")
kodon.update({"Stop Kod2": "UAA"})
print(kodon)