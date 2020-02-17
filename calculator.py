# import the calss #
from calc import calc

cal = calc()
print("Welcome to my calculator:")
print("-"*20)
print("1: Addition    \t\t    12: Sine in degrees")
print("2: Substraction    \t\t    13: Cosine in degrees")
print("3: Multiplication    \t\t    14: Tan in degrees")
print("4: Division    \t\t    15: Cosecant in degrees")
print("5: Sin in radians    \t\t    16: Secant in degrees")
print("6: Cosine in radians    \t\t    17: Cotan in degrees")
print("7: Tan is radians    \t\t    18: Natural log")
print("8: Cosecant in radians    \t\t    19: Base 10 log")
print("9: Secant in radians    \t\t    20: Log base 'x'")
print("10: Cotan in radians    \t\t    21: Square root")
print("11: pi    \t\t    22: Power of")
print("-"*20)

choice = ""
while True:
    try:
        choice = int(input("Enter a number of your choice: "))
    except:
        print("Please enter a valid number :( ")
    
    if choice == 1:
        n1 = float(input("Enter the first number to add: "))
        n2 = float(input("Enter the second number to add: "))
        cal.add(n1, n2)
    if choice == 2:
        n1 = float(input("Enter the first number to add: "))
        n2 = float(input("Enter the second number to add: "))
        cal.sub(n1, n2)
    if choice == 3:
        n1 = float(input("Enter the first number to add: "))
        n2 = float(input("Enter the second number to add: "))
        cal.mul(n1, n2)
    if choice == 4:
        n1 = float(input("Enter the numerator: "))
        n2 = float(input("Enter the denominator: "))
        cal.div(n1, n2)
    if choice == 5:
        n = float(input("Enter the number to find it Sine in rad: "))
        cal.sinrad(n)
    if choice == 6:
        n = float(input("Enter the number to find its Cosine in rad: "))
        cal.cosrad(n)
    if choice == 7:
        n = float(input("Enter the number to find its Tangent in rad: "))
        cal.tanrad(n)
    if choice == 8:
        n = float(input("Enter the number to find its Cosecant in rad: "))
        cal.cosecrad(n)
    if choice == 9:
        n = float(input("Enter the number to find its Secant in rad: "))
        cal.secrad(n)
    if choice == 10:
        n = float(input("Enter the number to find its Cotangent in rad: "))
        cal.cotrad(n)
    if choice == 11:
        cal.pie()
    elif choice == 12:
        n = float(input("Enter the number to find its Sine in degrees: "))
        cal.sindeg(n)
    elif choice == 13:
        n = float(input("Enter the number to find its Cosine in degrees: "))
        calc.cosdeg(n)
    elif choice == 14:
        n = float(input("Enter the number to find its Tan in degrees: "))
        calc.tandeg(n)
    elif choice == 15:
        n = float(input("Enter the number to find its Cosecant in degrees: "))
        calc.cosecdeg(n)
    elif choice == 16:
        n = float(input("Enter the number to find its Secant in degrees: "))
        calc.secdeg(n)
    elif choice == 17:
        n = float(input("Enter the number to find its Cotan in degrees: "))
        calc.cotdeg(n)
    elif choice == 18:
        n = float(input("Enter the number to find its natural log: "))
        calc.ln(n)
    elif choice == 19:
        n = float(input("Enter the number to find its Base 10 log: "))
        calc.logten(n)
    elif choice == 20:
        n = float(input("Enter the number to find its log: "))
        p = float(input("Enter desired base number: "))
        calc.logbasex(n, p)
    elif choice == 21:
        n = float(input("Enter the number to find its square root: "))
        calc.squreroot(n)
    elif choice == 22:
        n = float(input("Enter a number: "))
        p = float(input("Enter its power: "))
        calc.powerof(n, p)
    else:
        print("WARNING! Please enter a valid input.")
