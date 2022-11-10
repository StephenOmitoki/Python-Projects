import math

print("4")
print()

m= float((input("Enter the mass of the cart : ")))
print()
F = float(input("Enter the force to push the cart: "))
print()

g = 9.8

tmp1 = m*g
tmp2 = F/tmp1
tmp3= math.asin(tmp2)*180/math.pi

print("The angle of the ramp is ", (format(tmp3, '1.1f')),"degrees")


