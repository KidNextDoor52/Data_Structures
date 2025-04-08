#def reverse_words(s):
""" here we join the the words together then go through them from reverse then spliting them with the space
"""
#    return ' '.join(word[::-1] for word in s.split())
#print(reverse_words('hello there today'))
#
#import re
""" import re to be able to manipulate str 
"""
# CODE FOR REVERSING A STRING WHILE PAYING ATTENTION TO CAPS, SYMBOLS AND SPACES
#def is_palindrome(s):
""" Here we are creating a variable to hold the transformations (removal of symblols, spaces, and caps)

"""
#    cleaned_s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s.lower())
""" Here we are returning those transformations and seeing if the cleaned_s is equal to itself backwards
"""
#    return cleaned_s == cleaned_s[::-1]
#print(is_palindrome('Racecar'))


#only reverse alphabetic  characters

def reverse_only_letters(s):
    """ here i setting the variable letter to equal char for char in s if char.isalpha(). (checking for characters in word s if they are letters)
    """
    letters = [char for char in s if char.isalpha()]

    reversed_s = list(s)

    for i, char in enumerate(s):
        if char.isalpha():
            reversed_s[i] = letters.pop()

    return ''.join(reversed_s)

print(reverse_only_letters('a3b5643c!!&*(&de)'))
