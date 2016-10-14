#tell python to import whole module
import math
#tel python to import specific functions in a module
from math import sqrt
#tell python to import whole module and assign a variable
import math as ma
#tell python to import specific function of a module and assign a variable
from math import sqrt as asqrt

a = math.sqrt(36)
print(a)
b = ma.sqrt(36)
print(b)
c= sqrt(36)
print(c)
d = asqrt(36)
print(d)