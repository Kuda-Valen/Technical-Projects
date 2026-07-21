"""
    So in this file we are learnign how to manipulate strings

    == String methods ==
    A method is a built-in function that bellongs to a specific
    data type. You call it using dot notation: variable.method()
    .upper() converts string to ALL CAPS
    .lower() converts string to all lowercase
    .title() converts to Title Case
    .strip() removes leading and trailing whitespace
    .replace(old, new) swaps one substring for another
    .find(substring) returns the index of the first occurrence (-1 if not found)
    .split(delimiter) breaks a string into a list
    len(string) returns the character count

    == Indexing and Slicing ==
    Every character in a string has a position number called an index,
    starting from 0.
    name = 'Python'
    If we say print(name[0]) => it will print the char 'P'
    If we say print(name[0:3]) => it will print chars 'Pyt'
    If we say print(name[-3]) => it will print last three 'hon'
"""

name = "  Kudakwashe  "
surname = "Mukwasi"

print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
print(name.replace('Kudakwashe', 'Valentine'))
print(f"This should print new name starting with V: {name}")
print(f"The index of the first occurrence of K is: {name.find('K')}")
print(len(name))
#name.split()

for n in name:
    print(n)
