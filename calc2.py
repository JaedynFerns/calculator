typee = input("Enter the Math identity or physics: ")
try:
    if typee == "identity5":
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
        num_3 = float(input("Enter the third number: "))
        yet = pow(num_1, 2) + pow(num_2, 2) + pow(num_3, 2) + (2 * num_1 * num_2) + (2 * num_2 * num_3) + (2 * num_1 * num_3)
        print(str(num_1) + "^2 + " + str(num_2) + "^2 + " + str(num_3) + "^2 + 2 * " + str(num_1) + " * " + str(num_2) + " + 2 * " + str(num_2) + " * " + str(num_3) + " + 2 * " + str(num_1) + " * " + str(num_3))
        print("( x + y + z )^2")
        print(yet)
        
    elif typee == "identity6":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        yeet  = pow(num1, 3) + pow(num2, 3) + (3 * pow(num1, 2) * num2) + (3 * num1 * pow(num2, 2)) 
        print(str(num1) + "^3 + " + str(num2) + "^3 + 3 * " + str(num1) + "^2 * " + str(num2) + " + 3 * " + str(num1) + " * " + str(num2) + "^2")
        print("(x + y)^3")
        print(yeet)

    elif typee == "identity7":
        num3 = float(input("Enter the first number: "))
        num4 = float(input("Enter the second number: "))
        yeeet = pow(num3, 3) - pow(num4, 3) - (3 * pow(num3, 2) * num4) + (3 * num3 * pow(num4, 2))
        print(str(num3) + "^3 - " + str(num4) + "^3 - 3 * " + str(num3) + "^2 * " + str(num4) + "+ 3 * " + str(num3) + " * " + str(num4) + "^2")
        print("(x - y)^3")
        print(yeeet)

    elif typee == "identity8":
        num5 = float(input("Enter the first number: "))
        num6 = float(input("Enter the second number: "))
        yeeeet = (num5 + num6) * (pow(num5, 2) + pow(num6, 2) - (num5 * num6))
        print("( " + str(num5) + " + " + str(num6) + " )( " + str(num5) + "^2 + " + str(num6) + "^2 - " + str(num5) + " * " + str(num6) + " )")
        print("x^3 + y^3")
        print(yeeeet)

    elif typee == "identity9":
        num7 = float(input("Enter the first number: "))
        num8 = float(input("Enter the second number: "))
        yeeeeet = (num7 - num8) * (pow(num7, 2) + pow(num8, 2) + (num7 * num8))
        print("( " + str(num7) + " - " + str(num8) + " )( " + str(num7) + "^2 + " + str(num8) + "^2 + " + str(num7) + " * " + str(num8) + " )")
        print("x^3 - y^3")
        print(yeeeeet)
    elif typee == "speed":
        distance = float(input("Enter the total distance: "))
        unit = input("Enter whether km/h or m/s: ")
        time = float(input("Enter the total time: ")) 
        avspeed = distance / time
        print("Distance = " + str(distance) + "\nTime = " + str(time) + "\nAverage Speed = Total Distance/Total Time = " + str(distance) + "/" + str(time) + " = " + str(avspeed) + unit)
            
except:
    print("No variables allowed")