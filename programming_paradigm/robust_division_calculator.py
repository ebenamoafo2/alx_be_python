def safe_divide(numerator, denominator):

    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        try:
            # Attempt division
            result = num / denom
            return result
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Invalid input. Both arguments must be numeric."