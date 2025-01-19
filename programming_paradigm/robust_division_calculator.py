# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division and handle errors like division by zero and non-numeric inputs.
    
    Args:
        numerator: The numerator for division.
        denominator: The denominator for division.
    
    Returns:
        str: Result of division or error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        
        # Format result with one decimal place if necessary
        return f"The result of the division is {result:.1f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
