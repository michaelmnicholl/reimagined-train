exit = False
while exit == False:
    user_input = input('How shall i greet you? ')
    if user_input in ('Quit', 'Stop'):
        exit = True
    else:
        print(user_input)

