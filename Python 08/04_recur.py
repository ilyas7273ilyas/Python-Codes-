def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)

num = int(input('Enter the number: '))

print('Sum of series is: '+ str(sum(num)))   # Concatenation

print('Sum of series is: ', sum(num))   # simple

print(f'Sum of series is: {sum(num)}')  # Fstring