char=input("Enter a letter: ")
if len(char)==1 and char.isalpha():
    ch=char.lower()
    if ch in ['a','e','i','o','u']:
        print(f"{ch} is a vowel")
    else:
        print(f"{ch} is a constant")
else:
    print("Invalid Input, Enter correct input like (a-z)")