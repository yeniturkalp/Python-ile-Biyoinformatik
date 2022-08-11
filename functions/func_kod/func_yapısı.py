# İşlev, yalnızca çağrıldığında çalışan bir kod bloğudur.

# Parametre olarak bilinen verileri bir işleve geçirebilirsiniz.

# Bir işlev, sonuç olarak veri döndürebilir.


print("*** YAPISI ***")
def my_function():
  print("Bu bir fonksiyondur")

my_function() # fonksiyonu çağırır yani çalıştırır. Eğer bu kod olmasaydı f5'leyince geriye bir değer dönmezdi

print("*** ARGÜMAN EKLEME ***")

# birçok şekilde, fonksiyon içerisine argüman ekleyerek işlemler yapılabilir.

# işlem 1: tek parametre atayarak
print("--- TEK PARAMETRE ATAYARAK ---")
def my_function(konu):
  print(konu + " " + "Biyoinformatik")

my_function("Python ile") #konu parametresine "Python ile" kelimesini atayarak. Python ile biyoinformatik yazdırır 

#işlem 2: iki parametre atayarak
print("--- İKİ PARAMETRE ATAYARAK ---")

def my_function(konu1, konu2):
  print(konu1 + " ile " + konu2)

my_function("Python", "Biyoinformatik") #konu parametresine "Python ile" kelimesini atayarak. Python ile biyoinformatik yazdırır 

#işlem 3: *args: eğer dışarıdan parametreye kaç tane parametre atanacağı bilinmiyorsa parametre önüne * koyularak istenilen değerin seçilmesi sağlanır.

print("--- ARGS ---")

def my_function(*konu):
    print(konu[0] + " " + "biyoinformatik")# dışarıdan atanan değerin index nosu ile seçim yapılır
    
my_function("Python", "Python ile", "")


# işlem 4: eğer dışarıdan boş parametre gelmesi durumuna karşılık fonksiyon içerisine varsayılan bir değer atanabilir
print("--- VARSAYILAN DEĞER ATAYARAK ---")

def my_function(konu = "Python"):
    print(konu + " " + "Biyoinformatik")
    
my_function() # parametre atamadığımız için varsayılan değer atanır.
        