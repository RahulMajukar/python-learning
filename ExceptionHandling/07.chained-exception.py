# Chained Exceptions
# Python allows you to chain exceptions using the raise ... from syntax, which is useful for debugging.

# Example:

try:
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        raise ValueError("Something went wrong with the division") from e
except ValueError as e:
    print(f"Chained exception: {e}")