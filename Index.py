print("Faulty Calculator")
print("Enter your first number :")
num1 = int(input())
print("Enter your Operation")
opt = input()
print("Enter your second number :")
num2 = int(input())
if opt == "+":
    if num1==56 and num2==9:
        print("Your answer is 77")
    else:
        print("Your answer is :",num1+num2)
        if opt == "*":
            if num1==45 and num2==3:
                print("Your answer is 555")
            else:
                print("Your answer is :",num1*num2)
                if opt == "/":
                    if num1==56 and num2==4:
                        print("Your answer is 4")
                    else:
                        print("Your answer is :",num1/num2)
