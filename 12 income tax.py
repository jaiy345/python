a=int(input("enter your costing price"))
b=int(input("enter your GST %"))
c=(a/100*b)
sell=a+c
if sell>=250000:
    income='yes'
else:
    income='none'
print("GST AMOUNT:",c)
print("SELLING AMOUNT:",sell)
print("INCOME TAX:",income)
