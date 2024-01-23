loop = False
total = 0
index = 0
num = int(input("Enter a number: "))
while loop == False:
 num = str(num)
 digits = len(num) -1
 total = int(num[index]) + total
 index = index + 1
 if index > digits:
    print(f"The sum of the digits of this number is {total}")
    loop = True
