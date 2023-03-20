myDict={
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Item"
}
print("Options are",myDict.keys())
a=input("Enter the Hindi Word: ")

# .get(a), For avoiding error
print("Meaning of your word is: ",myDict.get(a))