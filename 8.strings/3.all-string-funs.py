# 1. capitalize()
# Converts the first character of the string to uppercase and the rest to lowercase.
s = "hello world"
print(s.capitalize())  # Output: Hello world


# 2. casefold()
# Converts the string to lowercase. It is more aggressive than lower().
s = "HELLO WORLD"
print(s.casefold())  # Output: hello world


# 3. center(width, fillchar)
# Centers the string within the specified width, optionally filling with the specified character.
s = "hello"
print(s.center(10, '-'))  # Output: --hello---


# 4. count(substring, start, end)
# Counts the occurrences of the substring in the string.
s = "hello world"
print(s.count("l"))  # Output: 3


# 5. encode(encoding, errors)
# Encodes the string using the specified encoding.
s = "hello"
print(s.encode("utf-8"))  # Output: b'hello'


# 6. endswith(suffix, start, end)
# Checks if the string ends with the specified suffix.
s = "hello world"
print(s.endswith("world"))  # Output: True


# 7. expandtabs(tabsize)
# Expands tabs in the string to the specified number of spaces.
s = "hello\tworld"
print(s.expandtabs(4))  # Output: hello   world


# 8. find(substring, start, end)
# Finds the first occurrence of the substring.
s = "hello world"
print(s.find("world"))  # Output: 6


# 9. format(*args, **kwargs)
# Formats the string using the specified arguments.
s = "Hello, {}!"
print(s.format("John"))  # Output: Hello, John!


# 10. format_map(mapping)
# Formats the string using a dictionary.
s = "Hello, {name}!"
print(s.format_map({"name": "John"}))  # Output: Hello, John!


# 11. index(substring, start, end)
# Finds the first occurrence of the substring, raises ValueError if not found.
s = "hello world"
print(s.index("world"))  # Output: 6


# 12. isalnum()
# Checks if all characters in the string are alphanumeric.
s = "hello123"
print(s.isalnum())  # Output: True


# 13. isalpha()
# Checks if all characters in the string are alphabetic.
s = "hello"
print(s.isalpha())  # Output: True


# 14. isascii()
# Checks if all characters in the string are ASCII characters.
s = "hello"
print(s.isascii())  # Output: True


# 15. isdecimal()
# Checks if all characters in the string are decimal characters.
s = "123"
print(s.isdecimal())  # Output: True


# 16. isdigit()
# Checks if all characters in the string are digits.
s = "123"
print(s.isdigit())  # Output: True


# 17. isidentifier()
# Checks if the string is a valid  identifier.
s = "hello"
print(s.isidentifier())  # Output: True


# 18. islower()
# Checks if all characters in the string are lowercase.
s = "hello"
print(s.islower())  # Output: True


# 19. isnumeric()
# Checks if all characters in the string are numeric.
s = "123"
print(s.isnumeric())  # Output: True


# 20. isprintable()
# Checks if all characters in the string are printable.
s = "hello world"
print(s.isprintable())  # Output: True


# 21. isspace()
# Checks if all characters in the string are whitespace.
s = "   "
print(s.isspace())  # Output: True


# 22. istitle()
# Checks if the string is title-cased.
s = "Hello World"
print(s.istitle())  # Output: True


# 23. isupper()
# Checks if all characters in the string are uppercase.
s = "HELLO"
print(s.isupper())  # Output: True


# 24. join(iterable)
# Joins an iterable of strings using the string as the separator.
s = "-"
print(s.join(["hello", "world"]))  # Output: hello-world


# 25. ljust(width, fillchar)
# Left-justifies the string within the specified width.
s = "hello"
print(s.ljust(10, '-'))  # Output: hello-----


# 26. lower()
# Converts the string to lowercase.
s = "HELLO"
print(s.lower())  # Output: hello


# 27. lstrip(chars)
# Removes leading characters (space is default).
s = "   hello"
print(s.lstrip())  # Output: hello


# 28. maketrans(x, y, z)
# Creates a translation table for use with translate().
s = "hello"
trans = s.maketrans("h", "j")
print(s.translate(trans))  # Output: jello


# 29. partition(separator)
# Splits the string into three parts: the part before the separator, the separator, and the part after the separator.
s = "hello world"
print(s.partition(" "))  # Output: ('hello', ' ', 'world')


# 30. replace(old, new, count)
# Replaces occurrences of the old substring with the new substring.
s = "hello world"
print(s.replace("world", "there"))  # Output: hello there


# 31. rfind(substring, start, end)
# Finds the last occurrence of the substring.
s = "hello world"
print(s.rfind("l"))  # Output: 9


# 32. rindex(substring, start, end)
# Finds the last occurrence of the substring, raises ValueError if not found.
s = "hello world"
print(s.rindex("l"))  # Output: 9


# 33. rjust(width, fillchar)
# Right-justifies the string within the specified width.
s = "hello"
print(s.rjust(10, '-'))  # Output: -----hello


# 34. rpartition(separator)
# Splits the string into three parts: the part before the last occurrence of the separator, the separator, and the part after the separator.
s = "hello world hello"
print(s.rpartition(" "))  # Output: ('hello world', ' ', 'hello')


# 35. rsplit(separator, maxsplit)
# Splits the string from the right at the specified separator.
s = "hello world hello"
print(s.rsplit(" ", 1))  # Output: ['hello world', 'hello']


# 36. rstrip(chars)
# Removes trailing characters (space is default).
s = "hello   "
print(s.rstrip())  # Output: hello


# 37. split(separator, maxsplit)
# Splits the string at the specified separator.
s = "hello world"
print(s.split())  # Output: ['hello', 'world']


# 38. splitlines(keepends)
# Splits the string at line breaks.
s = "hello\nworld"
print(s.splitlines())  # Output: ['hello', 'world']


# 39. startswith(prefix, start, end)
# Checks if the string starts with the specified prefix.
s = "hello world"
print(s.startswith("hello"))  # Output: True


# 40. strip(chars)
# Removes leading and trailing characters (space is default).
s = "   hello   "
print(s.strip())  # Output: hello


# 41. swapcase()
# Swaps case of all characters in the string.
s = "Hello World"
print(s.swapcase())  # Output: hELLO wORLD


# 42. title()
# Converts the first character of each word to uppercase.
s = "hello world"
print(s.title())  # Output: Hello World


# 43. translate(table)
# Translates the string using the specified translation table.
s = "hello"
trans = s.maketrans("h", "j")
print(s.translate(trans))  # Output: jello


# 44. upper()
# Converts the string to uppercase.
s = "hello"
print(s.upper())  #

# 45. zfill(width)
# Pads the string with zeros on the left to the specified width.
s = "42"
print(s.zfill(5))  # Output: 00042