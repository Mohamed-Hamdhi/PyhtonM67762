# Read the numbers like this:
# n = int(input())

# Print the result with print()

# Example of division, integer division and remainder:
#print(63 / 5)
#print(63 // 5)
#print(63 % 5)

students = int(input("Enter the Number of Students :"))
apples = int(input("Enter the Number of Apples :"))

remain = apples%students
numapples = apples//students

print("Apples that Each Student Have :",numapples)
print("Apples reamining :",remain)
