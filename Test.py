from math import sqrt

a = int(input())
b = int(input())
c = int(input())

delta = b**2 - 4*a*c

if delta < 0 :
    print("No roots, discriminant < 0")
elif delta == 0:
    n1 = -b/(2 * a)
    print("There is one root: {:.6f}".format(n1))
else:
    n12 = ((-b + sqrt(delta)) / (2 * a))
    n21 = ((-b - sqrt(delta)) / (2 * a))
    print("There are 2 roots: {:.6f}".format(n12) + " and {:.6f}".format(n21))

#dndkgdfgndkgndfkgdfgkjkfdgnf