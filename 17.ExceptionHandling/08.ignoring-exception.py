# Ignoring Exceptions
# You can choose to ignore exceptions by using the pass statement in the except block.

# Example:

try:
    result = 10 / 0
except ZeroDivisionError:
    pass  # Ignoring the exception silently