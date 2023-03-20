words = ['donkey', 'crow', 'parrot']

with open('file.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%$#@%$$@")
    with open('file.txt', 'w') as f:
        f.write(content)