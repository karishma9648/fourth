g=1
i=2
a=15
b=35
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        g=i
    i=i+1
print(g)