str=input("Enter the Username: ")
if(len(str)<10):
    print("Less than 10")
elif(len(str)==10):
    print("Equals to 10")
else:
    print("More than 10")