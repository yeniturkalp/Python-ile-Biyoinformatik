# liste elemanları döngü yapıları ile içerisinde gezilip, yazdırılabilir 


kodon = ['UAG', 'UUA', 'AGU', 'AGA', 'UCA', 'UUU', 'UCA', 'UUA']

# print("***** FOR DÖNGÜSÜ *****")
# for x in range(len(kodon)):
#     print(kodon[x])
    

print("***** WHİLE DÖNGÜSÜ *****")
i = 0

while i < len(kodon):
    print(kodon[i])
    i = i+1 # sonsuz dönğüye girmemek için değerini her zaman 1 arttırıyoruz