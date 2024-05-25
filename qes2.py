binary_Number = input("Please Write a binary number: ")

# Check each character manually
is_binary = True
for char in binary_Number:
    if char not in '01':
        is_binary = False
        break

if not is_binary:
    print("Invalid input, please enter a binary number")
else:
    decimal = int(binary_Number, 2)
    print("your decimal number: ", decimal)
