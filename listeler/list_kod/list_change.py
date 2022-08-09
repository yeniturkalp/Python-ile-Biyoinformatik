# liste öğelerini değiştirerek farklı değerler atıyabiliriz 

konu = ["Python", "ile", "Hesap Makinesi"]

print("***** İNDEX NO İLE DEĞER DEĞİŞTİRME *****")
konu[2] = "Biyoinformatik" # Hesap makinesi yerine biyoinformatik değeri atandı 

print(konu) # Python ile Biyoinformatik


print("***** NEGATİF İNDEXLEME İLE DEĞER DEĞİŞTİRME *****")
# negatif indexleme ile değer değiştirme 
konu[-1] = "Biyoinformatik"
print(konu)

print("***** DİZİN ARALIĞI İLE DEĞER DEĞİŞTİRME *****")
# dizin aralığı ile değer değiştirme 
konu[2:3] = ["Biyoinformatik"]
print(konu) 


print("***** İNSERT METODU İLE LİSTEYE ÖĞE EKLEME *****")
# insert metodu ile listeye öğe ekleme

konumuz = ["Python", "Biyoinfrmatik"]
konumuz.insert(1, "ile") # 2.indexe ile kelimesini yazdırmaya yarar
print(konumuz) 