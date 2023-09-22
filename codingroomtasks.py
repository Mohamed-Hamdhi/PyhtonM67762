#apple sharing
students = int(input("Enter the Number of Students :"))
apples = int(input("Enter the Number of Apples :"))

remain = apples%students
numapples = apples//students

print("Apples that Each Student Have :",numapples)
print("Apples reamining :",remain)


#area of triangle
b = int(input("Enter the Base of the triangle :"))
h = int(input("Enter the Height of the triangle :"))

# Print the result with print()
print("The Area of the Triangle is :",0.5*b*h)


#hello name

name = str(input("Enter your Name :"))

print("Hello ",name)

#next and previous number

num = int(input("Enter the Number you desire :"))

print("The next number for the number",num,"is",num+1)
print("The previous number for the number",num,"is",num-1)
