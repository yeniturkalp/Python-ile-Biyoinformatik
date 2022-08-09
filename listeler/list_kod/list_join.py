# iki farklı liste yapısını tek bir liste yapısına çevirebiliriz

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print("***** İŞLEM 1 *****")
list3 = list1 + list2
print(list3) # iki liste yapısını toplar ve farklı bir listeye ekler

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
print("***** İŞLEM 2 *****")
for x in list2:
  list1.append(x) # liste1 e liste 2 eklenir

print(list1) 


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
print("***** İŞLEM 3 *****")
list1.extend(list2) # liste1e liste2 eklenir
print(list1) 
