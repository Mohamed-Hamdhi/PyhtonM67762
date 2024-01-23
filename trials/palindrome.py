value = str(input("Enter a Value : "))

order = []
reverse = []
index = -1

for i in range(len(value)):
    order.append(value[index])
    index -= 1

for i in range(len(value)):
    reverse.append(value[i])

if reverse == order:
    print("it is a palindrome")

else:
    print("it is not a palindrome")