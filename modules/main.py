import my_pkg.Sub1_pkg.mod as m1
import my_pkg.Sub2_pkg.mod2 as m2
import my_pkg.Sub2_pkg.mod3 as m3
from my_pkg import some_numbers as sn

def add(x,y):
    return x-y

print(add(4,7))
print(m1.add(4,7))

m2.foo()
m3.bar()

print(sn)
#print(f"El maximo es: {max(some_numbers)}")