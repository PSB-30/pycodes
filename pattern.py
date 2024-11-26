#scope of this project is to print the pyramid patten

# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end='')
#     for j in range(i+1):
#         print("*",end=" ")
#     print(" ")

# Pyramid Pattern with Customization
def print_pyramid():
    # Get user input for the height and character
    n = int(input("Enter the height of the pyramid: "))
    char = input("Enter the character for the pyramid: ")

    print("\nPyramid Pattern:\n")
    for i in range(n):
        # Print leading spaces
        print(" " * (n - i - 1), end='')
        # Print pyramid characters
        print((char + " ") * (i + 1))
        
# Call the function
print_pyramid()
