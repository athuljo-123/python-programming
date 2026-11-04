year=int(input("enter the current year"))
future=int(input("enter the  future year"))
print("the leap year are")
for year in range(year,future+1,2):
    if((year%4==0 )and year%100!=0 or year%400==0):
        print(year)
