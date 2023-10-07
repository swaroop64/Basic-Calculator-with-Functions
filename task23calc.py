#Calculator using Functions

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return float(a)/float(b)
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print("Select operation.")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")
op=input()
if op=='+':
    print("Sum is",add(num1,num2))
elif op=='-':
    print("Difference is", subtract(num1,num2))
elif op=='*':
    print('Product is',mul(num1,num2))
elif op=='/':
    print('Division product is',divide(num1,num2))
else : 
    print("Invalid input!")
