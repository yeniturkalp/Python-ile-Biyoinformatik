set1 = {"a", "b" , "c"}
set2 = {"a", "b",1 }


print("UNION AND UPDATE")

set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)
print("****************************************************")

set1 = {"a", "b" , "c"}
set2 = {"a", "b",1 }

print("INTERSECTION_UPDATE")
set1.intersection_update(set2) # her iki yapıda ortak olan değerleri yazdırır
print(set1)

print("INTERSECTION")
set = set1.intersection(set2) # her iki yapıda ortak olan değerleri yazdırır

print(set)


set1 = {"a", "b" , "c"}
set2 = {"a", "b",1 }

print("SYMMETRIC_DIFFEREMCE_UPDATE")
set1.symmetric_difference_update(set2) # her iki yapıda ortak olan değerleri yazdırmaz
print(set1)

set1 = {"a", "b" , "c"}
set2 = {"a", "b",1 }

print("SYMMETRIC_DIFFEREMCE")
sets = set1.symmetric_difference(set2) # her iki yapıda ortak olan değerleri yazdırmaz

print(sets)






 

 
