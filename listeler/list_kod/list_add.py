# liste yapısına append(), insert() ve extend() metodları ile yeni bir eleman eklenebilir


# add metodu: sadece bir eleman eklenebilir
kodon = ["UAG","AGU", "AGA"]
kodon.append("UCA")
print("***** ADD METODU *****")
print(kodon) # UCA kodonu listeye eklenmiş halde yazdırır.

#insert metodu: 
print("***** INSERT METODU *****")
kodon.insert(1,"UUA") # 1. indexe UUA kodonunu ekler
print(kodon)


#extend metodu: birden fazla öğeyi aynı anda eklemeyi sağlar tuple, küme, sözlük vb. yapıları kullanarak öğeler eklenebilir
new_kodon = ["UUU","UCA","UUA"]
kodon.extend(new_kodon)
print("***** EXTEND METODU *****")
print(kodon)