msize =  10
stack = []

times = int(input("how many values do u want to enter in the list"))
while times > msize:
    print(f"values should be less than{msize} /nplease try again")
    times = int(input("how many values do u want to enter in the list"))


size = 0
for i in range(times):
    if size == msize:
        print("list full")
    
    else:
        num = input("Enter a value: ")

        stack.append(num)

val = -1
for i in stack:
    print(stack[val])
    val -=1
