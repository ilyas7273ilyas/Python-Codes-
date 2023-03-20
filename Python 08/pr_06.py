def inch_2_cm(inch):
    return (inch*2.54)

def cm_2_inch(cm):
    return (cm/2.54)

inch = float(input("Enter the length in inch: "))
print("Length in centimeter: ", inch_2_cm(inch))

cm = float(input("Enter the length in centimeter: "))
print("Length in centimeter: ", cm_2_inch(cm))