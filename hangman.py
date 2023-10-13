import random

import requests


word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

random_list = list(str(random.choice(WORDS)))
answer = []


final = random_list[2:-1]

length = len(final)

print("Guess the letters of the word which has 6 characters, you have 16 chances")
print(random_list[2:-1])

for i in range(length):
    print("*",end="")


for i in range(16):
    input1 = str(input("\nEnter the letter:"))
    
    for char in random_list[2:-1]:
        if char == input1:
            answer.append(char)
            correct = True


    if correct:
        print("\nLetter is correct")
        
    else:
        print("\nLetter is incorrect")
