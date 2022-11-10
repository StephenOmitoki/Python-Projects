print("3")
print()

finalaccountvalue = float((input("Enter final account value : ")))
print()
annualinterestrate = float(input("Enter annual interest in percent: "))
print()
years = float(input("Enter number of years : "))
print()

monthlyinterestrate = annualinterestrate/1200
tmp1 = (1+monthlyinterestrate)**(12*years)
tmp2 = finalaccountvalue/tmp1

print("Initial deposit value is " , float(tmp2))
print()
