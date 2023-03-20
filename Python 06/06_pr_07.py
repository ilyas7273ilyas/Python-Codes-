post=input("Enter the POST: ")
A=b=a=-1
A=post.find("ILIYAS") 
b=post.find("Iliyas")
a=post.find("iliyas")
if A!=-1 or b!=-1 or a!=-1:
    print("Found")
else:
    print("Not Found")