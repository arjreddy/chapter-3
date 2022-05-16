p_num = int(input("pocket number: "))

if p_num==0:
    print("green")
elif p_num<=10:
    if p_num%2==0:
        print("black")
    else:
        print("red")
elif p_num<=18:
    if p_num%2==0:
        print("red")
    else:
        print("black")
elif p_num<=28:
    if p_num%2==0:
        print("black")
    else:
        print("red")
elif p_num<=36:
    if p_num%2==0:
        print("red")
    else:
        print("black")
else:
    print("ERROR: invalid pocket number.")
