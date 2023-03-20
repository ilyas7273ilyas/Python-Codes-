#f = open('file.txt' , 'r')
f = open('file.txt')  #By default the mode is r
data = f.read()
data = f.read(8)  #reads 8 characters from the file
print(data)
f.close()