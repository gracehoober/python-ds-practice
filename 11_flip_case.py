def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
# need a result string
# loop through string
# compare letter to to_swap -> convert both to lowercase
    # if same
        # if letter to upper case == letter
            #add it to string but make it lowercase
        #if letter to lowercase == letter
            # add it to string but make it uppercase
    # if letter not the same add it to string
# return the string
    result = ""
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            # if letter.upper() == letter:
            #     result += letter.lower()
            # elif letter.lower() == letter:
            #     result += letter.upper()
            result += letter.lower() if letter.upper() == letter else letter.upper()
        else:
            result += letter
    return result
#think about "simpler solution"
#nested ternary??
