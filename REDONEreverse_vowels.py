def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?'
    """
    vowels = set('aeiouAEIOU')
    s = list(s) #converts string to a list to allow modification
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] not in vowels:
            i += 1 #move up one
        elif s[j] not in vowels:
            j -= 1 #move down one
        else:
            s[i], s[j] = s[j], s[i] # swap vowels
            i += 1
            j -= 1

    return ''.join(s) #convert list back to string


