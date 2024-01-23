num = int(input("Enter a number : "))
num = str(num)
entries = 0 
index = 1
index2 = -1
while len(num) != entries:
    if num[index] == num[index2]:
        index +=1
        index2 -= 1
        entries += 1
        print("its a plaindrome")

    else:
        print("not a palindrome")
        exit()