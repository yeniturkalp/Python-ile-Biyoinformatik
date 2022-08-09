# liste elemanları içerisinde çeşitli sorgular yaparak istenilen eleman bulunuabilir ve o listeden ayrıştırılabilir


kodon = ['UAG', 'UUA', 'AGU', 'AGA', 'UCA', 'UUU', 'UCA', 'UUA']
stop_kodon = []

# liste elemanlarını gezdik içerisinde UAG kodonu var ise onu boş olan stop kodonuna yazdırmayı sağlar
for x in kodon:
    if "UAG" in x:
        stop_kodon.append(x)
        
print(stop_kodon)
        