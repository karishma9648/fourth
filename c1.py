i=1
while (i<=5):
    n= int(input("Enter no."))
    if (i==1):
        big=small=n
    elif n>big:
        big=n
    elif n<small:   
        small=n
        i=i+1
print(big)
print(small)


