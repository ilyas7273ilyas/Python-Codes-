def star(n):
    for item in range(n,0,-1):
        print("*" * (item))
    
    for i in range(n):
        print("*" * (n-i))

n=star(3)