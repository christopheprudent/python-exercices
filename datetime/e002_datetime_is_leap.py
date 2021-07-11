# web solution
def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False

year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!= 0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")

print(leap_year(2012))
print(leap_year(2014))
