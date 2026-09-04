# Engineering-Solver
# Newton's Second Law
# F = m * a

print("================================")
print("   NEWTON'S SECOND LAW")
print("================================")

mass = float(input("Enter mass (kg): "))
acceleration = float(input("Enter acceleration (m/s^2): "))

force = mass * acceleration

print()
print("Calculation:")
print("F = m × a")
print(f"F = {mass} × {acceleration}")
print(f"F = {force} N")

print()
print(f"Answer: F = {force} N")