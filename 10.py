p_num = int(input("pennies count: "))
n_num = int(input("nickels count: "))
d_num = int(input("dimes count: "))
q_num = int(input("quarters count: "))

dollars=p_num*.01+n_num*.05+d_num*.1+q_num*.25
if dollars==1.0:
    print("Congrats! You Won!")
elif dollars>1.0:
    print("More than one dollar")
else:
    print("Less than one dollar")
