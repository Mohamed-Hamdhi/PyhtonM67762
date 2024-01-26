num = str(input("Enter a number : "))

index = 0
reverse = []
index2 = -1
order = []
while len(num) != index:
    order.append(num[index])
    index +=1
    reverse.append(num[index2])
    index2 -= 1


if order == reverse :
    print("it is a palindrome")

else:
    print("it is not a palindrome")
