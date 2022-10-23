#Exercise 3: Slice list into 3 equal chunks and reverse each chunk
from audioop import reverse
from pickle import TRUE


sample_list=[11,45,8,23,14,12,78,45,89]
l=[]
l1=[]
for i in sample_list[0:3]:
    sample_list.remove(i)
    l.append(i)
    

for i in sample_list[0:3]:
    sample_list.remove(i)
    l1.append(i)
    

    
print(l1)    
print(l)
print(sample_list)
l.reverse()
l1.reverse()
sample_list.reverse()
print("after reverseing:",l)
print("after reverseing:",l1)
print("after reverseing:",sample_list)



