s = "(]"
values = [")","]","}"]
original = ["()","{}","[]"]

for i in s:
    for j in values:
        for z in original:
            if i + j == z:
                print(True)
                
            else:
                print(False)