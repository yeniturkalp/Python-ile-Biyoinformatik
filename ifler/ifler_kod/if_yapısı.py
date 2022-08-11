# if bloğu eğer anlamına gelir. Yani; bir koşulun doğru olup olmadığını kontrol ederek, şart koşarak kodun daha düzenli çalışmasını sağlar.

#Mantıksal operatörker bu şartları oluşturmada yardımcı olur 

# Eşittir: a == b
# Eşit Değil: a != b
# Daha az: a < b
# a küçük veya eşit: a <= b
# a büyüktür: a > b
# a, b'den büyük veya eşittir: a >= b

#örnek: iki sayıların birbiri ile kıyası
print("ÖRNEK 1")
a = 33
b = 200
if b > a:
  print("b sayısı a sayısından büyüktür!")#print kodu if blogunun 4 satır içerisinde olmalıdır.
  
  
#örnek2: iki liste yapısının eleman sayılarını karşılaştırma
print("ÖRNEK 2")
stop_kodon = ["UAA","UAG","UGA"]
star_kodon = ["AUG"]

if len(stop_kodon) > len(star_kodon):
    print("Stop kodon sayısı star kodon sayısından fazladır!")