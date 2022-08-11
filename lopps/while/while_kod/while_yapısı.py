kodon = {
    
    "Stop Kod": "UAA",
    "Stop Kod2": "UAG",
    "Start Kod": "AUG"     
    }

i = 2

print("*** WHİLE DÖNGÜ ***")
while i < len(kodon): # kodon sözlüğü eleman sayısından küçük olana kadar içinde ki elemanları gez ve yazdır
    print(kodon)
    i +=1 # sonsuz döngüye girmesin diye i yi her döngüde 1 arttırır ve koşul doğru olana kadar böyle devam eder.


print("*** BREAK ***")    
i = 0
while i < 6:
    print(i)
    if i == 4:
        break # i 4'e eşit olduğunda döngüyü durdurur 
    i +=1 
 
print("*** CONTIUNE ***")  
i = 0
while i < 6:
    i +=1 
    if i == 4:
        continue # i 4'e eşit olduğunda 4'ü atlar ve döngüye devam ederek değerleri yazdırır.  
    print(i)

    
print("*** ELSE ***")

i = 0 
while i < 10:
    print(i)
    i += 1
else:
    print("i sayısı haddini aşmıştır :D") # döngü artık doğru olmadığında else bloğu ile bildiri mesajı verilir



