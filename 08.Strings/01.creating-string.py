# Using single quotes to create a string
single_quote_str = 'Hello, World!'
print(single_quote_str)

# Using double quotes to create a string
double_quote_str = "Hello, World!"
print(double_quote_str)

# Triple quotes are useful for multi-line strings.
triple_quote_str = """Hello,
World!"""
print(triple_quote_str)

# Similar to triple double quotes, these can also span multiple lines.
triple_single_quote_str = '''Hello,
World!'''
print(triple_single_quote_str)

# Concatenating strings using the + operator
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + ", " + str2 + "!"
print(concatenated_str)

# You can convert other data types to a string using the str() function.
number = 123
str_number = str(number)
print(str_number)

# The format() method allows for inserting variables into a string.
name = "John"
formatted_str = "Hello, {}!".format(name)
print(formatted_str)

# Using f-Strings (Formatted String Literals)
# Introduced in Python 3.6, f-strings provide a concise way to embed expressions inside string literals.
name = "John"
f_string = f"Hello, {name}!"
print(f_string)

# Using the join() method to concatenate a list of strings with a separator
words = ["Hello", "World"]
joined_str = ", ".join(words)
print(joined_str)

# Raw strings treat backslashes as literal characters.
# Useful for regular expressions and Windows file paths.
raw_str = r"C:\Users\John"
print(raw_str)

# Using the repr() function to get a string representation of an object
repr_str = repr("Hello\nWorld")
print(repr_str)

# Creating a repeated string using the * operator
repeated_str = "Hello" * 3
print(repeated_str)

# Creating a Unicode string
unicode_str = u"Hello, World!"
print(unicode_str)

# Creating a bytes string
byte_str = b"Hello, World!"
print(byte_str)
