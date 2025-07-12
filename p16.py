n1=int(input("Please enter your point:"))
if(n1<50):
    print("entered point is 3rd point:",n1)
elif(n1>50):
    print("entered point is 2nd point:",n1)
elif(n1>75):
    print("entered point is 1st point:",n1)
elif(n1<33):
    print("entered point is failuare:",n1)
n1=float(input("Enter the marks of math-"))
n2=float(input("Enter the marks of Science-"))
n3=float(input("Enter the marks of Biology-"))
n4=float(input("Enter the marks of Chemistry-"))
n5=float(input("Enter the marks of Python-"))
total=n1+n2+n3+n4+n5
print("total marks of all subject is-",total)
