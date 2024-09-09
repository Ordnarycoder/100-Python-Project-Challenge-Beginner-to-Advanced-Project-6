def reverse_word():
    word = input("Please enter a word\n")
    word = word.lower()
    reversed_word = []  
    for letter in reversed(word):  
        reversed_word.append(letter)
    palindrom_word = "".join(reversed_word)  
    
    if word == palindrom_word:
        print("It's a palindrome word!")  
    else:
        print("It's not a palindrome word")

reverse_word()
