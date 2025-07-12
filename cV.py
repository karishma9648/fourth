#call by value(immutable data type)
def x(n):
    print(id(n))
    print(n)#100
    n=n+1
    print(id(n))
    print(n)#101
n=100
x(n)
print(id(n))
print(n)
a=100
b=a
print(id(a))
#call by reference
def changeme(mylist):