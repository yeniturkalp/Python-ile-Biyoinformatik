kodon = {'UAG', 'UUA', 'AGU', 'AGA', 'UCA', 'UUU', 'UCA', 'UUA'}

print("REMOVE")
kodon.remove("UAG") # UAG kodonunu siler eğer UAG yapı içerisinde olmasaydı hata verirdi
print(kodon)

print("DISCARD")
kodon.discard("UUA") # UUA kodonunu siler eğer UUA yapı içerisinde olmasaydı hata vermezdi
print(kodon)

print("POP")
kodon.pop() # değeri belirtmediğimiz için son öğeyi siler 
print(kodon)
