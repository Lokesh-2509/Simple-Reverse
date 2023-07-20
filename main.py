def reverse_string(s):
    return s[::-1]
if __name__ == "__main__":
    input_str = input("Enter the string: ")
    result = reverse_string(input_str)
    print("Reversed string:", result)
