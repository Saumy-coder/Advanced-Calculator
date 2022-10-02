
import math
import cmath
from traceback import print_tb


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def factorial(x):
    sum = 1
    for i in range(1,x+1):
        sum = sum*i
    return sum

def calculation():
    print("For basic Operations, write the number and operations")

    num = float(input("Number 1: "))
    operator = input("Operator: ")
    sum=0

    if(operator=='+'):
        num2 = float(input("Number 2: "))
        sum= add(num,num2)
    elif(operator=='-'):
        num2 = float(input("Number 2: "))
        sum = sub(num,num2)
    elif(operator=='/'):
        num2 = float(input("Number 2: "))
        sum = divide(num,num2)
    elif(operator=='*'):
        num2 = float(input("Number 2: "))
        sum = multiply(num,num2)
    elif(operator=='!'):
        sum = factorial(num)
    
    elif(operator=='P' or operator=='p'):
        num2 = float(input("Number 2: "))
        nfact = factorial(num)
        rfact =factorial(num-num2)
        sum = nfact/rfact

    elif(operator=='C'or operator=='P'):
        num2 = float(input("Number 2: "))
        nfact = factorial(num)
        rfact =factorial(num2)
        nrfact = factorial(num - num2)
        sum = (nfact)/(rfact*nrfact)
    print(sum)

def equation():
    print("Choose any option and put the number beside it-")
    print("1. Quadratic")
    print("2. Pair of linear equation in 2 variables")
    print("3. Linear equation in 1 variable")
    opt = int(input("Option: "))
    if(opt==1):
        print("In the form of ax^2 + bx + c = 0")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        alpha = ((-1*b)+math.sqrt(b**2-(4*a*c)))/(2*a)
        beta = ((-1*b)-math.sqrt(b**2-(4*a*c)))/(2*a)
        print(alpha,beta)
    
    elif(opt==2):
        print("In the form of \na1x + b1y + c1 = 0 \na2x + b2y + c2=0")
        a1 = float(input("a1: "))
        b1 = float(input("b1: "))
        c1 = float(input("c1: "))
        a2 = float(input("a2: "))
        b2 = float(input("b2: "))
        c2 = float(input("c2: "))

        solx = ((b1*c2)-(b2*c1))/((b2*a1)-(b1*a2))
        soly = ((c1*a2)-(c2*a1))/((b2*a1)-(b1*a2))

        print('x = '+solx+', y = ',soly)
    
    elif(opt==3):
        print("In the form of ax + b = 0")
        a = float(input("a: "))
        b = float(input("b: "))
        sum = (-1)*b/a
        print(sum)
    
def trigo():
    print("Choose the following number for the trigonometry function- ")
    print("1. sine \n2. cosine \n3. tangent \n4. cosecant \n5. secant \n6. cotangent")
    opt = int(input("Option: "))
    angle = float(input("Enter angle (IN DEGREES): "))
    angle = math.radians(angle)
    if opt==1:
        value = math.sin(angle)
    elif opt==2:
        value = math.cos(angle)
    elif opt==3:
        value = math.tan(angle)
    elif opt==4:
        value = 1/math.sin(angle)
    elif opt==5:
        value = 1/math.cos(angle)
    elif opt==6:
        value = 1/math.tan(angle)
    print(value)

def invtrigo():
    print("Choose the following number for the inverse trigonometry function- ")
    print("1. sine \n2. cosine \n3. tangent \n4. cosecant \n5. secant \n6. cotangent")
    opt = int(input("Option: "))
    value = float(input("Enter value: "))
    if opt==1:
        angle = math.asin(value)
    elif opt==2:
        angle = math.acos(value)
    elif opt==3:
        angle = math.atan(value)
    elif opt==4:
        angle = 1/math.asin(value)
    elif opt==5:
        angle = 1/math.acos(value)
    elif opt==6:
        angle = 1/math.atan(value)
    angle = math.degrees(angle)
    print("The angle is in degrees")
    print(angle)

def logarithm():
    print("If you want base to be e, then just simply write 91830192 :)")
    base = float(input("Base = "))
    value = float(input("Number = "))
    if(base!=91830192):
        log = math.log(value,base)
    else:
        log = math.log(value,math.e)
    print(log)

def complexno():
    print("Following operations can be performed- ")
    print("1. Add two complex numbers \n2. Subtract two complex numberx \n3. Multiply two complex numbers \n4. Divide two complex numbers \n5. Modulus of complex number \n6. Argument of complex number \n7. Logarithm of complex number \n8. Conjugate of complex number")
    opt = int(input("Option: "))
    if(opt == 1):
        x1 = float(input("Re(z1): "))
        y1 = float(input("Im(z1): "))
        z1 = complex(x1,y1)
        x2 = float(input("Re(z2): "))
        y2 = float(input("Im(z2):  "))
        z2 = complex(x2,y2)
        sum = z1 + z2
    elif opt==2:
        x1 = float(input("Re(z1): "))
        y1 = float(input("Im(z1): "))
        z1 = complex(x1,y1)
        x2 = float(input("Re(z2): "))
        y2 = float(input("Im(z2):  "))
        z2 = complex(x2,y2)
        sum = z1-z2
    elif opt==3:
        x1 = float(input("Re(z1): "))
        y1 = float(input("Im(z1): "))
        z1 = complex(x1,y1)
        x2 = float(input("Re(z2): "))
        y2 = float(input("Im(z2):  "))
        z2 = complex(x2,y2)
        sum = z1*z2
    elif opt==4:
        x1 = float(input("Re(z1): "))
        y1 = float(input("Im(z1): "))
        z1 = complex(x1,y1)
        x2 = float(input("Re(z2): "))
        y2 = float(input("Im(z2):  "))
        z2 = complex(x2,y2)
        sum = z1/z2
    elif opt==5:
        x1 = float(input("Re(z): "))
        y1 = float(input("Im(z): "))
        z1 = complex(x1,y1)
        sum = abs(z1)
    elif opt==6:
        x1 = float(input("Re(z): "))
        y1 = float(input("Im(z): "))
        z1 = complex(x1,y1)
        sum = cmath.phase(z1)
    
    elif opt==7:
        x1 = float(input("Re(z): "))
        y1 = float(input("Im(z): "))
        z1 = complex(x1,y1)
        base = float(input("Base: "))
        sum10 = cmath.log(10,z1)
        sume = cmath.log(cmath.e,z2)
        sum = cmath.log(base,z1)
        print("Logarithm with base 10 is "+sum10+" \n Logarithm with base e is "+sume)
    
    elif opt == 8:
        x1 = float(input("Re(z): "))
        y1 = float(input("Im(z): "))
        z1 = complex(x1,y1)
        sum = z1.conjugate()
    print(sum)

def maincalci():
    print("Hello there welcome to advanced calculator")
    print("Choose the option you want to perform")
    print("1. Basic Operations - Addition, Subtraction, Multiplication, Division as well as factorial, Permutation and Combination\n2. Solving an equation \n3. Trigonometry \n4. Inverse Trigonometry \n5. Logarithm \n6. Operations on Complex Number")
    opt = int(input("Option: "))
    if opt==1:
        calculation()
    elif opt==2:
        equation()
    elif opt==3:
        trigo()
    elif opt==4:
        invtrigo()
    elif opt==5:
        logarithm()
    elif opt==6:
        complexno()
    else:
        print("Choose valid option")
    print("Press y to continue or any other key to exit")
    state = input("")
    if(state=='y'):
        maincalci()
    else:
        exit

maincalci()