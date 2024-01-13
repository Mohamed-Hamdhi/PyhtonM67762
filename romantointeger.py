s = "LVIII"
total = 0
num = []
for i in s:
    if i == "I":
        num.append(1)

    elif i == "V":
        num.append(5)

    elif i == "X":
        num.append(10)

    elif i == "L":
        num.append(50)

    elif i == "C":
        num.append(100)
            
    elif i == "D":
        num.append(500)

    elif i == "M":
        num.append(1000)
        
for i in num:
    total += i
    

print(total)
