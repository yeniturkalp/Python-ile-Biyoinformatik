# for döngüsü veya sorgu ile set yapısının içerisinde ki yapılara erişilebilir

kodon = {'UAG', 'UUA', 'AGU', 'AGA', 'UCA', 'UUU', 'UCA', 'UUA'}

print(" BİRİNCİ YÖNTEM")
for x in kodon:
    print(x)
    
print(" İKİNCİ YÖNTEM")
if "UAG" in kodon:
    print("UAG geni set yapısı içerisinde vardır.")