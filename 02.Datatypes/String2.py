# Indexing
print(str1[4])  # Printing the 4th character of the string

# String Repetition
print(str1 * 2)  # Printing the string twice

# String Concatenation
print(str1 + "hello")  # Printing the concatenation of str1 and "hello"

# len(): Returns the length of the string.
s = "Hello"
print(len(s))  # Output: 5

# .lower() and .upper(): Convert the string to lowercase or uppercase.
s = "Hello"
print(s.lower())  # Output: "hello"
print(s.upper())  # Output: "HELLO"


# .strip(): Removes leading and trailing whitespace (or specified characters).
s = "  Hello  "
print(s.strip())  # Output: "Hello"

# .replace(old, new): Replaces occurrences of old substring with new substring.
s = "Hello, World!"
print(s.replace("Hello", "Hi"))  # Output: "Hi, World!"

# .split(): Splits the string into a list of substrings based on a delimiter.
s = "apple,banana,orange"
print(s.split(","))  # Output: ['apple', 'banana', 'orange']


# .join(iterable): Joins elements of an iterable (e.g., list) into a string, using the string as a delimiter.
fruits = ['apple', 'banana', 'orange']
print(", ".join(fruits))  # Output: "apple, banana, orange"

# .find(sub) and .index(sub): Return the lowest index of substring sub. .find() returns -1 if not found, .index() raises an exception.
s = "Hello, World!"
print(s.find("World"))  # Output: 7
print(s.index("World"))  # Output: 7

# .count(sub): Returns the number of occurrences of substring sub in the string.
s = "Hello, World!"
print(s.count("o"))  # Output: 2

# .islower() and .isupper(): Check if all characters in the string are lowercase or uppercase, respectively.
s1 = "hello"
s2 = "HELLO"
print(s1.islower())  # Output: True
print(s2.isupper())  # Output: True

# .capitalize(): Converts the first character to uppercase and the rest to lowercase.
s = "hello world"
print(s.capitalize())  # Output: "Hello world"

# .swapcase(): Converts uppercase characters to lowercase and vice versa.
s = "Hello World"
print(s.swapcase())  # Output: "hELLO wORLD"

# .zfill(width): Pad a numeric string with zeros on the left, making the total string length width.
s = "42"
print(s.zfill(5))  # Output: "00042"

# .find(sub) and .rfind(sub): Return the lowest index of substring sub. .find() searches from the beginning, .rfind() searches from the end.
s = "Hello, World!"
print(s.find("o"))    # Output: 4
print(s.rfind("o"))   # Output: 8

# .index(sub) and .rindex(sub): Like .find() and .rfind(), but raise ValueError if sub is not found.
s = "Hello, World!"
print(s.index("o"))    # Output: 4
print(s.rindex("o"))   # Output: 8

# .isdecimal(): Returns True if all characters in the string are decimal characters (digits), otherwise False.
s1 = "12345"
s2 = "123.45"
print(s1.isdecimal())   # Output: True
print(s2.isdecimal())   # Output: False

# .istitle(): Returns True if the string is in title case (first character of each word is uppercase, all other characters are lowercase), otherwise False.
s1 = "Hello World"
s2 = "Hello world"
print(s1.istitle())   # Output: True
print(s2.istitle())   # Output: False


# .partition(sep): Splits the string at the first occurrence of sep, and returns a tuple containing the part before sep, the sep itself, and the part after sep.
s = "Hello, World!"
print(s.partition(","))   # Output: ('Hello', ',', ' World!')


# .rpartition(sep): Splits the string at the last occurrence of sep, and returns a tuple containing the part before sep, the sep itself, and the part after sep.
s = "Hello, World!"
print(s.rpartition(" "))   # Output: ('Hello,', ' ', 'World!')


# .center(width, fillchar): Returns a centered string of length width. Padding is done using the specified fillchar (default is space).
s = "Python"
print(s.center(10, '*'))   # Output: '**Python**'


# .ljust(width, fillchar): Returns a left-justified string of length width. Padding is done using the specified fillchar (default is space).
s = "Python"
print(s.ljust(10, '-'))   # Output: 'Python----'

# .rjust(width, fillchar): Returns a right-justified string of length width. Padding is done using the specified fillchar (default is space).
s = "Python"
print(s.rjust(10, '*'))   # Output: '****Python'


# .expandtabs(tabsize): Expands tabs in the string to multiple spaces. By default, tab characters are replaced by spaces assuming a tab size of 8.
s = "Hello\tWorld"
print(s.expandtabs(4))   # Output: 'Hello   World'

# .strip(chars), .lstrip(chars), .rstrip(chars): Remove leading/trailing/all occurrences of chars (default is whitespace) from the string.
s = "***Hello***"
print(s.strip('*'))   # Output: 'Hello'

# .title(): Returns a version of the string where each word starts with an uppercase character, all remaining characters are lowercase.
s = "hello world"
print(s.title())   # Output: 'Hello World'


# .translate(table): Returns a copy of the string where each character has been mapped through the given translation table.
table = str.maketrans('aeiou', '12345')
s = "hello world"
print(s.translate(table))   # Output: 'h2ll4 w4rld'
