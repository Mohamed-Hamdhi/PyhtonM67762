prime = False
while prime == False:
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        print("Number is prime")
        prime = True
    elif num == 2: 
        print("Number is prime")
    else:
        print("Number is not prim")