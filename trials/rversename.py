value = str.lower(input("Enter a name : "))

reverse = []
index = -1
for i in value:
    reverse.append(value[index])
    index -= 1

for i in reverse:
    print(i,end="")


print()
