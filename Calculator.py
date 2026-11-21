import math
while True:
    print("                                 CALCULATOR                               ")
    print("SELECT OPERATION")
    print("1. ADDITION")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. SQUARE ROOT")
    print("6. EXPONENTIATION")
    print("7. MODULUS (REMAINDER)")
    print("8. FLOOR DIVISION")
    print("9. FACTORIAL")
    print("10. LOGARITHM")
    print("11. TRIGONOMETRIC FUNCTIONS")
    print("12. CUBE ROOT")
    print("13. GCD")
    print("14. LCM")
    print("15. NUMBER SYSTEM CONVERTER")
    print("16. VIEW CALCULATION HISTORY")
    print("17. CLEAR HISTORY")
    print("18. EXIT")
    choice = input("Enter your choice (1-18): ")
    try:
        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print("The result of addition is:",result)
            with open("calculation_history.txt", "a") as file:
                file.write(f"Addition: {num1} + {num2} = {result}\n")
        elif choice=='2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            print("The result of subtraction is:",result)
            with open("calculation_history.txt", "a") as file:
                file.write(f"Subtraction: {num1} - {num2} = {result}\n")
        elif choice=='3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print("The result of multiplication is:",result)
            with open("calculation_history.txt", "a") as file:
                file.write(f"Multiplication: {num1} * {num2} = {result}\n")
        elif choice=='4':   
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Division: {num1} / {num2} = Error (Division by zero)\n")
            else:
                result = num1 / num2
                print("The result of division is:",result)
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Division: {num1} / {num2} = {result}\n")
        elif choice=='5':
            num = float(input("Enter a number: "))
            if num < 0:
                print("Error: Square root of negative number is not defined.")
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Square Root: {num} = Error (Negative number)\n")
            else:
                result = math.sqrt(num)
                print("The square root of", num, "is:", result)
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Square Root: {num} = {result}\n")
        elif choice=='6':
            num=float(input("Enter a number: "))
            power=float(input("Enter power: "))
            if num == 0 and power < 0:
                print("Error: Zero cannot be raised to a negative power.")
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Exponentiation: {num} ** {power} = Error (Zero raised to negative power)\n")
            elif num < 0 and not power.is_integer():
                print("Error: Complex results are not supported.")
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Exponentiation: {num} ** {power} = Error (Complex result)\n")
            else:
                result = num ** power
                print("The result of exponentiation is:", result)
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Exponentiation: {num} ** {power} = {result}\n")
        elif choice=='7':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2==0:
                print("Error: Modulus by zero is not allowed.")
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Modulus: {num1} % {num2} = Error (Modulus by zero)\n")
            else:
                result = num1 % num2
                print("The result of modulus is:",result)
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Modulus: {num1} % {num2} = {result}\n")
        elif choice=='8':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Floor Division: {num1} // {num2} = Error (Division by zero)\n")
            else:
                result = num1 // num2
                print("The result of floor division is:",result)
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Floor Division: {num1} // {num2} = {result}\n")
        elif choice=='9':
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Error: Factorial of negative number is not defined.")
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Factorial: {num} = Error (Negative number)\n")
            else:
                result = math.factorial(num)
                print("The factorial of", num, "is:", result)
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Factorial: {num} = {result}\n")
        elif choice=='10':
            num = float(input("Enter a number: "))
            base = float(input("Enter the base (default is e): ") or math.e)
            if num <= 0 or base <= 0 or base == 1:
                print("Error: Invalid Logarithm Input.")
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Logarithm: {num} (base {base}) = Error (Invalid Input)\n")
            else:
                result = math.log(num, base)
                print("The logarithm of",num,"with base",base,"is:", result)
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Logarithm: {num} (base {base}) = {result}\n")
        elif choice=='11':
            print("SELECT TRIGONOMETRIC FUNCTION")
            print("1. SIN")
            print("2. COS")
            print("3. TAN")
            print("4. COT")
            print("5. SEC")
            print("6. COSEC")
            trig_choice = input("Enter your choice (1-6): ")
            if trig_choice == '1':
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)
                result = round(math.sin(radians), 10)
                print("The sine is:", result)
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Sine: {angle} degrees = {result}\n")
            elif trig_choice == '2':
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)
                result = round(math.cos(radians), 10)
                print("The cosine is:", result)
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Cosine: {angle} degrees = {result}\n")
            elif trig_choice == '3':
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)
                if angle % 180 == 90:
                    print("Error: Tangent is undefined at this angle.")
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Tangent: {angle} degrees = Error (Undefined tangent)\n")
                else:
                    result = round(math.tan(radians), 10)
                    print("The tangent is:", result)
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Tangent: {angle} degrees = {result}\n")
            elif trig_choice == '4':
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)
                if angle % 180 == 0:
                    print("Error: Cotangent is undefined at this angle.")
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Cotangent: {angle} degrees = Error (Undefined cotangent)\n")
                else:
                    result = round(1 / math.tan(radians), 10)
                    print("The cotangent is:", result)
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Cotangent: {angle} degrees = {result}\n")
            elif trig_choice == '5':
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)
                if angle % 180 == 90:
                    print("Error: Secant is undefined at this angle.")
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Secant: {angle} degrees = Error (Undefined secant)\n")
                else:
                    result = round(1 / math.cos(radians), 10)
                    print("The secant is:", result)
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Secant: {angle} degrees = {result}\n")
            elif trig_choice == '6':
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)
                if angle % 180 == 0:
                    print("Error: Cosecant is undefined at this angle.")
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Cosecant: {angle} degrees = Error (Undefined cosecant)\n")
                else:
                    result = round(1 / math.sin(radians), 10)
                    print("The cosecant is:", result)
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Cosecant: {angle} degrees = {result}\n")
            else:
                print("Invalid choice for trigonometric function.")
                with open("calculation_history.txt", "a") as file:  
                    file.write("Error: Invalid choice for trigonometric function\n")
        elif choice=='12':
            num = float(input("Enter a number: "))
            result = math.cbrt(num)
            print("The cube root of", num, "is:", result)
            with open("calculation_history.txt", "a") as file:
                file.write(f"Cube Root: {num} = {result}\n")
        elif choice=='13':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = math.gcd(num1, num2)
            print("The GCD of", num1, "and", num2, "is:", result)
            with open("calculation_history.txt", "a") as file:
                file.write(f"GCD: {num1} and {num2} = {result}\n")
        elif choice=='14':
            num1=int(input("Enter first number: "))
            num2=int(input("Enter second number: "))
            result=math.lcm(num1,num2)
            print("The LCM of", num1, "and", num2, "is:", result)
            with open("calculation_history.txt", "a") as file:
                file.write(f"LCM: {num1} and {num2} = {result}\n")
        elif choice=='15':
            print("SELECT NUMBER SYSTEM CONVERSION")
            print("1. Decimal to Binary")
            print("2. Decimal to Octal")
            print("3. Decimal to Hexadecimal")
            print("4. Binary to Decimal")
            print("5. Octal to Decimal")
            print("6. Hexadecimal to Decimal")
            conversion_choice = input("Enter your choice (1-6): ")
            if conversion_choice == '1':
                num = int(input("Enter a decimal number: "))
                if num < 0:
                    result ="-" + bin(num)[3:]
                    print(f"Binary representation of {num} is: {result}")
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Decimal to Binary: {num} = {result}\n")
                else:
                    result = bin(num)[2:]
                    print(f"Binary representation of {num} is: {result}")
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Decimal to Binary: {num} = {result}\n")
            elif conversion_choice == '2':
                num = int(input("Enter a decimal number: "))
                if num < 0:
                    result ="-" + oct(num)[3:]
                    print(f"Octal representation of {num} is: {result}")
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Decimal to Octal: {num} = {result}\n")
                else:
                    result = oct(num)[2:]
                    print(f"Octal representation of {num} is: {result}")
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Decimal to Octal: {num} = {result}\n")
            elif conversion_choice == '3':
                num = int(input("Enter a decimal number: "))
                if num < 0:
                    result ="-" + hex(num)[3:].upper()
                    print(f"Hexadecimal representation of {num} is: {result}")
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Decimal to Hexadecimal: {num} = {result}\n")
                else:        
                    result = hex(num)[2:].upper()
                    print(f"Hexadecimal representation of {num} is: {result}")
                    with open("calculation_history.txt", "a") as file:
                        file.write(f"Decimal to Hexadecimal: {num} = {result}\n")
            elif conversion_choice == '4':
                num = input("Enter a binary number: ")
                result = int(num, 2)
                print(f"Decimal representation of binary {num} is: {result}")
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Binary to Decimal: {num} = {result}\n")
            elif conversion_choice == '5':
                num = input("Enter an octal number: ")
                result = int(num, 8)
                print(f"Decimal representation of octal {num} is: {result}")
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Octal to Decimal: {num} = {result}\n")
            elif conversion_choice == '6':
                num = input("Enter a hexadecimal number: ")
                result = int(num, 16)
                print(f"Decimal representation of hexadecimal {num} is: {result}")  
                with open("calculation_history.txt", "a") as file:
                    file.write(f"Hexadecimal to Decimal: {num} = {result}\n")
            else:
                print("Invalid choice for number system conversion.")
                with open("calculation_history.txt", "a") as file:
                    file.write("Error: Invalid choice for number system conversion\n")
        elif choice=='16':
            try:
                with open("calculation_history.txt", "r") as file:
                    history = file.read()
                    if history:
                        print("Calculation History:")
                        print(history)
                    else:
                        print("No calculation history found.")
            except FileNotFoundError:
                print("No calculation history found.")
        elif choice=='17':
            with open("calculation_history.txt", "w") as file:
                file.write("")
            print("Calculation history cleared.")  
        elif choice=='18':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid operation.")
            continue
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        with open("calculation_history.txt", "a") as file:
                    file.write("Error:Invalid Input (ValueError)\n")     
    except OverflowError:
        print("Error: The result is too large to calculate.")
        with open("calculation_history.txt", "a") as file:
            file.write("Error: Numerical result too large (OverflowError)\n")

