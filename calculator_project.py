#CALCULATOR PROJECT
import math
#it is a function where we will know if we dont type number
def getting_num(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("This is not a number! " \
            "pls write number")


#we are going to make list for one number operator and two number operators
one_number_ops = ['sqrt','abs','!','log','sin','cos','tan']
two_number_ops = ['+','-','*','/','//','%','**','avg','percent']

print("===== CALCULATOR =====")
print("Type for one number operator: sqrt,abs,!,log,sin,cos,tan")
print("Type for two number operator:+,-,*,/,//,%,**,avg,percent")
print("Type 'quit' to exit")

while True:
    op = input("\nEnter operator:").strip().lower()
    if op == 'quit':
        print("Goodbye! " \
        "Thank you for using calculator")
        break
    if op in one_number_ops:
        num=getting_num("Enter number :")

        if op == "sqrt":
            if num<0:
                result="ERROR!!! // no square root of negative number"
            else:
                result=math.sqrt(num)
        elif op=="abs":
            result=abs(num)
        elif op=="!":
            if num<0 or num!=int(num):
                result="ERROR!!! // use a whole number, 0 or more "
            else:
                result=math.factorial(int(num))   #factorial can be done only on integers
        elif op=="log":
            if num<0:
                result="ERROR!!! // log of negative number does not exist" 
            elif num<=0:
                result="ERROR!!! // log only works for numbers greater than 0"
            else:
                result=math.log10(num)
        elif op=="sin":
            result=round(math.sin(math.radians(num)), 10)
        elif op=="cos":
            result=round(math.cos(math.radians(num)), 10)
        elif op=="tan":
            result=round(math.tan(math.radians(num)), 10)
    elif op in two_number_ops:
        num1=getting_num("Enter first number: ")
        num2=getting_num("Enter second number: ")
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op in ["/", "//", "%"] and num2 == 0:
            result = "Error: cannot divide by zero"
        elif op == "/":
            result = num1 / num2
        elif op == "//":
            result = num1 // num2
        elif op == "%":
            result = num1 % num2
        elif op == "**":
            try:
                result = num1 ** num2
            except OverflowError:
                result = "Error: result is too large"
        elif op == "avg":
            result = (num1 + num2) / 2
        elif op == "percent":
             result = num1 / 100 * num2
    else:
        result = "Invalid operator, try again"
        
    print("Result:", result)
    