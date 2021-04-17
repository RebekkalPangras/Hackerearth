vowels = ['a','e','i','o','u','A','E','I','O','U']
n = int(input())

def findStringKind(word):
    lowercase = True
    uppercase = True
    for letter in word:
        if letter.isupper() and letter not in vowels:            
                uppercase = False
        elif letter.islower() and letter not in vowels:
                lowercase = False
        elif not lowercase and not uppercase:
            return "ugly string"
    return "lovely string"

for i in range(n):
    word = input()
    result = findStringKind(word)
    print(result)
