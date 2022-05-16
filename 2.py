l1 = int(input("Enter length of first rectangle: "))
w1 = int(input("Enter width of first rectangle: "))
l2 = int(input("Enter length of second rectangle: "))
w2 = int(input("Enter width of second rectangle: "))

area1 = l1*w1
area2 = l2*w2

if area1>area2:
    print("first rectangle has greater area.")
elif area2>area1:
    print("second rectangle has greater area.")
elif area1==area2:
    print("Both rectangles have same area.")

