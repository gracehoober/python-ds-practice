def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    #evens_to_doubled = {n: n * 2 for n in nums if n % 2 == 0}
    # a_words = {w for w in words if w.startswith("a")}
    count = {}
    for letter in phrase:
        if count.get(letter):
            count[letter]+=1
        else:
            count[letter] = 1
    #count = {count[letter]+=1 if count.get(letter) else count[letter] = 1 for letter in phrase}
    return count
