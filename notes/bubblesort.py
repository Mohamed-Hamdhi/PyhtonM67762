pi = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
 
print(pi)
pilist = len(pi)
 
switchinlist = True
 
while switchinlist == True:
    for stage in range(0, pilist - 1):
        if pi[stage] > pi[stage + 1]:
            temporary = pi[stage]
            pi[stage] = pi[stage + 1]
            pi[stage + 1] = temporary
            print(pi)
        switchinlist = True