def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def reverse_string(s):
    return s[::-1]

def main():
    user_input = input("Enter a string: ")
    print(f"Number of vowels: {count_vowels(user_input)}")
    print(f"Reversed string: {reverse_string(user_input)}")

if __name__ == "__main__":
    main()
