import math
p=0
eps=0.001
a=0
x=0.5
p=math.sin(x)
n=2
while (a/(math.factorial(n)))>eps:
    a=-math.sin(x**n)
    n+=1
print("p=",p)