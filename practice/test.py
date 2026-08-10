def is_anagram(s1, s2):
    # Remove spaces and convert to lowercase if necessary
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

# Test
print(is_anagram("Schoolmastersi","The classroom is"))  # Output: True
print(is_anagram("rat", "tar"))    # Output: True
