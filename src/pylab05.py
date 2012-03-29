

# Phone numbers as words 
# NOTE: CHALLENGING. OPTIONAL.

DICTFILE = 'linux.txt'
PHONEPAD = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}

# WRITE THE TWO FUCTIONS number2pseudowords  AND number2english AND MAKE SURE THEY PASS THE TESTS.


def number2pseudowords(number):
    """Returns all pseudo words for the given number. Most of those will not be English words.
    
    >>> pseudo = number2pseudowords("248")
    >>> 'BGT' in pseudo
    True
    >>> 'BIT' in pseudo
    True
    >>> pseudo = number2pseudowords("5865")
    >>> len(pseudo)
    81
    >>> pseudo = number2pseudowords("2273")
    >>> len(pseudo)
    108
    >>> 'CCSF' in pseudo
    True
    """
    
    master_list = []
    ret_list = []
    #print(PHONEPAD[2])
    for num in number:
        master_list.append(PHONEPAD[int(num)])
    
    for c in master_list[0]:        
        get_combinations(master_list, c, ret_list)
    
    return ret_list
    
        

def get_combinations(short_array, concat_value, store_array):
    #for each letters in array, i need to add concat_value to array[i]
    # then, when I'm done with the row i append to store_array
    if len(short_array) == 1:        
        store_array.append(concat_value)
    else:
        for b in short_array[1]:
            get_combinations(short_array[1:], concat_value+b, store_array)
        
         
    
    

def number2english(number):
    """Returns upper case words for the given partial phone number.
 
    >>> words = number2english("468")
    >>> "GET" in words
    False
    >>> "GOT" in words
    True
    >>> "HOT" in words
    True
    >>> len(words)
    13
    >>> words = number2english("5865")
    >>> "JUNK" in words
    True
    >>> len(words)
    3
    """
    
    word_list = number2pseudowords(number)
    ret = set()
    with open(DICTFILE, 'r') as english:
        for word in english:
            word = word.strip().upper()
            if word in word_list:
                ret.add(word)
    
    #print(ret)
    return ret
    



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    number = input("Please enter a partial phone number: ")
    print(list(number2english(number)))
    

    
