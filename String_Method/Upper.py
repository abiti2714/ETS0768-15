# Example of upper() method

def main():
    # 1. Standardizing case for comparison
    string_1 = "Python"
    string_2 = "PYTHON"

    # Using upper() for comparison
    result_1 = string_1.upper() == string_2.upper()
    # Both strings become "PYTHON", so the result is True.
    print(result_1)  # Expected output: True

    # 2. Handling mixed-case strings
    string_3 = "PyThoN is FuN"

    # Convert all lowercase letters to uppercase
    result_2 = string_3.upper()
    # Non-alphabetic characters remain unchanged.
    print(result_2)  # Expected output: PYTHON IS FUN


if __name__ == "__main__":
    main()
