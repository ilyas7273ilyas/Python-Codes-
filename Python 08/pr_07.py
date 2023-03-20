def remove_strip(str, word):
    newstr = str.replace(word, '')
    return newstr.strip()

this  = '       No one is Happy      '
print(this)
print(this.strip())

n= remove_strip(this, "one")
print(n)