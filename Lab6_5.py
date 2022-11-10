import math

print("5")
print()

m = float((input("Enter the mass of the cart : ")))
print()
a = float(input("Enter the angle to push the cart: "))
print()

g = 9.8

tmp1 = m*g
F = tmp1 * math.sin(a*math.pi/180)


print("The angle of the ramp is ", (format(F, '2.2f')),"Newtons")
