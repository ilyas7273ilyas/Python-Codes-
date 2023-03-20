# num=int(input('Enter the no: '))
# i=1
# f=1
# while i<=num:
#     f=f*i
#     i=i+1
# print("Factorial: " + str(f))

num=int(input('Enter the no: '))
f=1
for i in range(1,num+1):
    f=f*i
print("Factorial: " + str(f))