def is_vowol(character):
    vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] 
    if character in vowels:
        return True
    else:
        return False

print(is_vowol('a'))
print(is_vowol('b'))
print(is_vowol('E'))
print(is_vowol('Z'))
