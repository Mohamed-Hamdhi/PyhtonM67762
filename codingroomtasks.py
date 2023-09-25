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

#sum of 3
num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))
num3 = int(input("Enter Third Number :"))

print("The Sum is :",num1+num2+num3)

#input/print hours and secs
secs = int(input("Enter the number of seconds :"))

mins = secs//60
hours = mins//60

print("mins passed :",mins)
print("hours passed :",hours)

#input or print two timestamps
hour1 = int(input("Enter First Hour :"))
min1 = int(input("Enter First Minute :"))
sec1 = int(input("Enter First Second"))

hour2 = int(input("Enter Second Hour :"))
min2 = int(input("Enter Second Minute :"))
sec2 = int(input("Enter Second Second"))

#two digits
num = int(input("Enter A number : "))

strnum = str(num)

listnum = list(strnum)

print(listnum[-2],listnum[-1])


#swap digits
num = int(input("Enter a number :"))

strnum = str(num)

listnum = list(strnum)

print(listnum[1]+listnum[0])


#last two digits
num = int(input("Enter A number : "))

strnum = str(num)

listnum = list(strnum)

print(listnum[-2]+listnum[-1])

#tens digit
num = int(input("Enter A number : "))

strnum = str(num)

listnum = list(strnum)

print(listnum[-2])

#sum of digits
num = int(input("Enter A number : "))

strnum = str(num)

listnum = list(strnum)

num1 = int(listnum[0])
num2 = int(listnum[1])
num3 = int(listnum[2])

print(num1+num2+num3)

#digit after deciaml point
num = float(input("Enter a Float number :"))

strnum = str(num)

listnum = list(strnum)

for i in listnum:
    
    if i == ".":
        print(listnum[listnum.index(".")+1])

