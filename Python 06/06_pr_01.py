num1=int(input("Enter the first Number: "))
num2=int(input("Enter the second Number: "))
num3=int(input("Enter the third Number: "))
num4=int(input("Enter the fourth Number: "))

if(num1>num2 and num1>num3 and num1>num4):
    print("First Number is Greatest Number")
elif(num2>num3 and num2>num4):
    print("Second Number is Greatest Number")
elif(num3>num4):
    print("Third Number is Greatest Number")
else:
    print("Fourth Number is Greatest Number")