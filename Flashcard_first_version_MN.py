#Flashcard_first_version_MN
"""This flashcard program allows the user to ask for a glossary entry.
In response, the program randomly picks an entry from all glossary entries. It shows the entry.
After the user presses return, the program shows the definition of that particular entry.
The user can repeatedly ask for an entry and also
has the option to quit the program"""
from random import *
def show_flashcard():
    """Show the user a random key and ask them to define it.  Show the definition
when the user presses return"""
    random_key = choice(list(glossary))
    print('Define: ', random_key)
    input('Press return to see the correct definition')
    print(glossary[random_key])
glossary = {'word1':'definition1',
            'word2':'definition2',
            'word3':'definition3'}
#The interactive loop
exit = False
while exit != True:
    user_input = input('Enter S to show a flashcard or Q to quite: ')
    if user_input == 'Q':
        exit = True
    elif user_input == 'S':
        show_flashcard()
    else:
        print('You must only enter S or Q, please try again')
