def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    phrase = [char for char in phrase if not char == ' ']
    left = 0
    right = len(phrase) - 1


    while left < right:
        if not phrase[left].lower() == phrase[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True