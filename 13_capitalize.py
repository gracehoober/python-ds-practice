def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    letters = list(phrase)
    letters[0] = letters[0].upper()
    return ''.join(letters)