text=input("Enter the Text: ")

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe this" in text):
    spam=True
elif("click this" in text):
    spam=True
else:
    spam=False

if(spam):     #By Default it is True
    print("This text is SPAM")
else:
    print("This text is not SPAM")