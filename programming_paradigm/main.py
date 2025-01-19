# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Command line interface for the division calculator.
    Accepts two arguments: numerator and denominator.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Extract arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform division and print result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
