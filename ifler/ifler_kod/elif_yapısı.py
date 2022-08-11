# mantıksal bir kod yazarken sadece if bloğu ile tamamen mantıksal bir kod yazmış olmayız eğer if bloğu şartı çalışmaz ise elif bloğunu kullanırız.

#örnek: iki sayıda eşit ise nolacak?

a = 200
b = 200
if b > a:
  print("b sayısı a sayısından büyüktür!")# her iki değerde eşit olmadığu için bu şart çalışmaz
elif b == a:
    print("İki sayıda eşittir!")