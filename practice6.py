#Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
l=[2,5,4,6,8,5,11]
l1=[5,9,1,3,7,9,23]
a=[]
for i,j in zip(l,l1) :
    if i%2==0 or j%2!=0:
        a.append(i) or a.append(j)
        print(a)

        
        
        
        

    