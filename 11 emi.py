p=int(input('enter your principal amount:'))
r=int(input("enter rate of interest:"))
t=int(input("enter time you invested:"))
ir=r/(12*100)
mn=12*t
emi=p*ir*(pow((1+ir),mn))/((1+ir)**mn-1)
print("Emi:",emi)
