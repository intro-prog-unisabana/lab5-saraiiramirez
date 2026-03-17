import utils_calc

while True:
    opcion = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()

    if opcion == "exit":
        break

    if opcion not in ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide","absolute"]:
        print("Invalid option!")
        continue

    if opcion == "absolute":
        num = float(input("Enter the number:\n"))
        resultado = utils_calc.absolute(num)
    else:
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))

        if opcion == "add":
            resultado = utils_calc.add(num1, num2)
        elif opcion == "subtract":
            resultado = utils_calc.sub(num1, num2)
        elif opcion == "multiply":
            resultado = utils_calc.multiply(num1, num2)
        elif opcion == "divide":
            resultado = utils_calc.divide(num1, num2)
        elif opcion == "exponent":
            resultado = utils_calc.exponent(num1, num2)
        elif opcion == "modulo":
            resultado = utils_calc.modulo(num1, num2)
        elif opcion == "floor_divide":
            resultado = utils_calc.floor_divide(num1, num2)

    print(f"The result is: {resultado}")