

characters = input()

vowels = 'aeiou'

consonants = 'abcdfghjklmnpqrstvwxyz'

for i in characters:
    if i in vowels:
        print("vowel")
    elif i in consonants:
        print("consonant")
    else:
        break