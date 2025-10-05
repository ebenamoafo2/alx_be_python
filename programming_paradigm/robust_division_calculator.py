def safe_divide(numerator, denominator):
    """Safely perform division with error handling."""
    try:
        num = float(numerator)
        denom = float(denominator)

        try:
            result = num / denom
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."