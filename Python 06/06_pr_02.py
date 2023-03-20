m1=int(input("Enter the marks of first subject: "))
m2=int(input("Enter the marks of second subject: "))
m3=int(input("Enter the marks of third subject: "))
if(m1<33 or m2<33 or m3<33):
    print("You are Fail due to marks in individual subject is les than 33")
elif((m1+m2+m3)/3<40):
    print("Total marks is less than 40%, So you are Fail")
else:
    print("Congratulations! You are PASS")