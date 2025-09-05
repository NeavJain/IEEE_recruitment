word = []
t = int(input("How many words do you want to check:"))

for i in range(0,t):
    check = ""
    inp = input(f"Enter word {i+1}:")
    check=inp[::-1] #reverses the word
    if inp == check:
         word.append(inp)         #adds it to the list if palindrome
print(f"there are {len(word)} words which are palindrome")
print(word)