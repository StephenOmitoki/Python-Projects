import math
print()

print("1")
print()

width = float(input("Enter the width of a rectangle : "))
print()
length = float(input("Enetr the height of a rectangle : "))
print()
perimeter = 2*(length + width)
area = length * width
tmp = ((length**2) + (width**2))
diagonal = math.sqrt(tmp)
print("The perimeter is " , perimeter)
print("The area is " , area)
print("The diagonal is " , diagonal)

print()



finalaccountvalue = float((input("Enter final account value : ")))
print()
annualinterestrate = float(input("Enter annual interest in percent: "))
print()
years = input("Enter number of years : ")
print()

monthlyinterestrate = annualinterestrate/1200
tmp1 = (1+monthlyinterestrate)**12
tmp2 = finalaccountvalue/tmp1

print("Initial deposit value is " , float(tmp2))
print()
