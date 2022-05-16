
age = int(input("Enter your age: "))

if age<=1:
    print("Infant.")
elif age>1 and age<13:
    print("Child.")
elif age<20:
    print("Teenage.")
else:
    print("Adult")
