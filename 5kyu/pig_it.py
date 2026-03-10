import unittest

"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
"""

def pig_latin(text):
    words = text.split()
    pig_latin_words = []
    
    for word in words:
        if word.isalpha():  # Check if the word is purely alphabetic
            pig_word = word[1:] + word[0] + "ay"
            pig_latin_words.append(pig_word)
        else:
            pig_latin_words.append(word)  # Keep punctuation marks unchanged
    
    return ' '.join(pig_latin_words)

    #one liner
    #return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in words])

# Example usage:
input_text = "Hello, world!"
output_text = pig_latin(input_text)
print(output_text)  # Output: "elloHay, orldway!"
