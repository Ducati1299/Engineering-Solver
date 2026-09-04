# Engineering-Solver
# Main Program

from physics.newton import calculate_force

print("========================================")
print("          ENGINEERING SOLVER")
print("========================================")

print()
print("1. Physics")
print("2. Calculus")
print("3. Electrical Engineering")
print("4. Engineering Mechanics")
print("5. Unit Converter")
print("0. Exit")

print()

choice = input("Select: ")

if choice == "1":
    print()
    print("---------- PHYSICS ----------")
    print("1. Newton's Second Law")

    physics_choice = input("Select: ")

    if physics_choice == "1":
        mass = float(input("Enter mass (kg): "))
        acceleration = float(input("Enter acceleration (m/s^2): "))

        force = calculate_force(mass, acceleration)

        print()
        print("Calculation:")
        print("F = m × a")
        print(f"F = {mass} × {acceleration}")
        print(f"F = {force} N")

        print()
        print(f"Answer: F = {force} N")

    else:
        print("Invalid selection.")

elif choice == "2":
    print("Calculus module is coming soon.")

elif choice == "3":
    print("Electrical Engineering module is coming soon.")

elif choice == "4":
    print("Engineering Mechanics module is coming soon.")

elif choice == "5":
    print("Unit Converter is coming soon.")

elif choice == "0":
    print("Goodbye!")

else:
    print("Invalid selection.")