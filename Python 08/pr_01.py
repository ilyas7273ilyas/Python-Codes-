def max(n1, n2, n3):
    if(n1>n2 and n1>n3):
        return n1
    elif n2>n3:
        return n2
    else:
        return n3

m = max(25, 28, 50);
print('Maximum number is: ' + str(m))