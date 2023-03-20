letter='''Dear <|NAME|>, 
Greeting from Nowhere. I am too happy.
Thanks and regards,
Date: <|DATE|>'''

name=input("Enter ur Name \n")
date=input("Enter Date \n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)