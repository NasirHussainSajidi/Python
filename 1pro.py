print("to make a simple calculator by using python")
a=int(input("enter a first No ="))
x= input("enter operator =")
b=int(input("enter a second No ="))
if x == "+":
    print("value is =", a+b)
elif x == "-":
    print("value is =", a-b)
elif x == "*":
    print("value is = ", a*b)
elif x == "/":
    print("value is = ", a/b)
elif x == "**":
    print("value id = ", a**b)
elif x == "%":
    print("value id = ", a%b)
else:
    print("you enter wrong operator")


