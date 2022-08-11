# if, elif ile mantıksal algoritma kurabiliriz fakat her iki koşula da sağlamayan durumlarda mevcuttur daha anlaşılır ve çalışan kod yazmamız için else bloğunuda kullanırız.

#else eğer iki blokta çalışmaz ise bu blok çalışsın diyerek blok döngüsünü bitirir ve ekrana cevabı yazdırır


#örnek: iki değerde sağlanmıyorsa
a = 210
b = 200
if b > a:
  print("b sayısı a sayısından büyüktür!")# her iki değerde eşit olmadığu için bu şart çalışmaz
elif b == a:
    print("İki sayıda eşittir!")# iki sayı eşit olmadığı için blok çalışmaz
else:
    print("A sayısı B sayısından büyüktür!")# iki şart doğru değilse bu şart doğrudur der ve cevabı yazdırır
    

    
