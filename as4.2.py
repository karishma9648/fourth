'''length and breadth of rectangle and radius of a circle are input throught the keyboard
l=int(input("please enter the length of the rectangle-"))
print(l)
b=int(input("please enter the length of the rectangle-"))
print(b)
r=int(input("please enter the radius of the circle-"))
print(r)

wap to program to calculate the area  and perimeter  of the rectangle  and the area and circumference of the circle'''

len=float(input("please enter length of the rectangle-"))
br=float(input("please enter breadth of the rectangle-"))
ar=len*br
print("area of the rectangle-",ar)
pr=2*(len+br)
print("perimeter of the rectangle-",pr)
r=float(input("please enter radius of the circle-"))
ar=2*(3.14)*r*r
print("area of the circle is-",ar)
cr=2*3.14*r
print("circumference of the circle is-",cr)