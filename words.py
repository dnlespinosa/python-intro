for char in ['word', 'wordtwo', 'wordthree']:
    print(char.upper())

def print_upper_words(words):
    '''Takes your list of words and changes the letters to uppercase'''
    for char in ['word', 'wordtwo', 'wordthree']:
        print(char.upper())

def print_upper_words2(words):
    '''Takes your list of words and changes the letters to uppercase, only if the word begins with the letter 'e'''
    for char in words:
        if char[0]=='e':
            print(char.upper())


def print_upper_words3(words, must_start_with):
    '''Takes your list of words and changes the letters to uppercase, only if the word begins with the letter 'e'''
    must_start_with = input('please enter letters     ')

    for char in words:
        for letter in must_start_with:
            if char[0]==letter:
                print(char.upper())