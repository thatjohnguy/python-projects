#  _______  _______  ___      _______  __   __  ___      _______  _______  _______  ______   
# |       ||   _   ||   |    |       ||  | |  ||   |    |   _   ||       ||       ||    _ |  
# |       ||  |_|  ||   |    |       ||  | |  ||   |    |  |_|  ||_     _||   _   ||   | ||  
# |       ||       ||   |    |       ||  |_|  ||   |    |       |  |   |  |  | |  ||   |_||_ 
# |      _||       ||   |___ |      _||       ||   |___ |       |  |   |  |  |_|  ||    __  |
# |     |_ |   _   ||       ||     |_ |       ||       ||   _   |  |   |  |       ||   |  | |
# |_______||__| |__||_______||_______||_______||_______||__| |__|  |___|  |_______||___|  |_|
# John Omoluabi

# checklist
# ***********
# 1. define functions needed; add, subtract, multiply, divide
# 2. print options to user
# 3. ask for values
# 4. call functions
# 5. persist program until user wants to exit

def add(a,b):
    return f"{a} + {b} = {int(a) + int(b)}"
def subtr(a,b):
    return f"{a} - {b} = {int(a) - int(b)}"
def mult(a,b):
    return f"{a} x {b} = {int(a) * int(b)}"
def divi(a,b):
    return f"{a} / {b} = {int(a) / int(b)}"

print("A - Addition")
print("B - Subtraction")
print("C - Multiplication")
print("D - Division")


while True:
    choice=input("What Operation would you like to do?(A-D)?")
    choice=choice.lower()
    match choice:
        case "a":
            a=input("first operand: ")
            b=input("second operand: ")
            print(add(a,b))
            
        case "b":
            a=input("first operand: ")
            b=input("second operand: ")
            print(subtr(a,b))
            
        case "c":
            a=input("first operand: ")
            b=input("second operand: ")
            print(mult(a,b))
            
        case "d":
            a=input("first operand: ")
            b=input("second operand: ")
            print(divi(a,b))
            