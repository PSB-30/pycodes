def check_occurrence(word, a):
    print("Given string is:", word)
    if a in word:
        return word.count(a)
    else:
        return 0

# Example usage
mystr = "mystring"
char = "t"
occurrences = check_occurrence(mystr, char)
print(f"The character '{char}' occurs {occurrences} time(s) in '{mystr}'.")
