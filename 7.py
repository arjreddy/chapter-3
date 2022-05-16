
color1 = input("Enter first color: ")
color2 = input("Enter second color: ")


if (color1=='red' and color2=='yellow') or (color2=='red' and color1=='yellow'):
    print("orange")
elif (color1=='red' and color2=='blue') or (color2=='red' and color1=='blue'):
    print("purple")
elif (color1=='yellow' and color2=='blue') or (color2=='yellow' and color1=='blue'):
    print("green")
else:
    print("Wrong Input...")

