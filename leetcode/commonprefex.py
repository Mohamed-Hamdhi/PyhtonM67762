strings = ["flower","flow","flight"]

prefix = []
for i in range(len(strings) - 1):
    j = 0
    while j < min(len(strings[i]), len(strings[i+1])):
        if strings[i][j] != strings[i+1][j]:
            break
        j += 1
    prefix.append(strings[i][:j])

for i in prefix[1]:
    print(i,end="")


print()
