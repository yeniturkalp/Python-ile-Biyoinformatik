# tuplelere erişim [] parantez içerisine index no yazarak ulaşabiliriz. Negatif indexleme, dizin aralığı ile erişimde sağlanmaktadır

kodon = ('UAG', 'UUA', 'AGU', 'AGA', 'UCA', 'UUU', 'UCA', 'UUA')

#index no ile erişim 
print("***** İNDEX NO İLE *****")
print(kodon[2]) #AGU yazdırır

#negatif indexleme
print("***** NEGATİF İNDEXLEME *****")
print(kodon[-2]) #UCA yazdırır

# dizin aralığı 
print("***** DİZİN ARALIĞI *****")
print(kodon[2:5]) # AGU, AGA, UCA yazdırır

#şartlama

print("***** ŞARTLAMA *****")
for x in kodon:
    if "UAG" in x:
        print("Bu kodon demetinde: "+ str(x) + " durdurma kodonu vardır.")

