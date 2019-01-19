## making leap year by fuction method
def is_leap(year):
    if year%400==0:
     return "leap"
    elif year%4==0 and year%100!=0:
        return "leap"
    else:
        return "non leap year"
year=int(input())
print(is_leap(year))

# leap year by single line if-else

x=int(input("enter a year"))
result="leap year" if x%400==0 else "leap year" if x%4==0 and x%100!=0 else "non leap year"
print(result)
