# iki şekilde sözlük yapısı kopyalanabilir

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(" YÖNTEM 1 ")
mydict = thisdict.copy()
print(mydict)

print(" YÖNTEM 2 ")
mydict2 = dict(thisdict)
print(mydict2)

