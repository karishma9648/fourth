#wap to input a number as year to check year is LEAP or not.....
'''year=int(input("please enter a year:-"))
if (year%400==0):
    if(year%100==0):  
        print(year)
        print("this year is leap year")
    else:
        print(year)
        print("this year is not leap.")'''

year=int(input("please enter a year:-"))
if(year%4==0 and year%100!=0 or year%400==0 ):

    print(year)
    print("this year is leap year")
else:
    print(year)
    print("this year is not leap.")
