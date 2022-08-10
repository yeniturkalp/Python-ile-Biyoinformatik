# set yapısına öğe ekleme 2 şekilde yapılır.

# 1.yöntem: add() metodu ile ekleme yapılır
print("YÖNTEM 1")
kodon = {'UAG', 'UUA', 'AGU'}
kodon.add('UUA')
print(kodon)
# 2.yöntem: update metodu ile sözlük yapısı veya istenilen başka bir yapı ekleme yapılır


print("YÖNTEM 2")
kodon2 = {'UUU', 'UCA'}
kodon.update(kodon2) # set yapısını set yapısına ekler

kodon3 = ['AGA', 'GUA']
kodon.update(kodon3)
print(kodon)

