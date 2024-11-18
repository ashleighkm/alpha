
# Display my name
name = input("Enter your name: ")

# Accept n as input from the user
n = int(input("Enter the number of characters to display from the left: "))

# Display n characters from left
print("First", n, "characters:", name[:n])

# Count the number of vowels in the name
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in name if char in vowels)
print("Number of vowels:", vowel_count)

# Reverse the name
reversed_name = name[::-1]
print("Reversed name:", reversed_name)