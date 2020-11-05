from voice import *     #speak(text): returns nothing, my_word(): returns text from speech
from lichess_login import *     #login(): returns nothing, create_game(command): returns nothing, make_move(move):returns nothing 
from transform import *     #transform(text): returns move
from cnv import *       #validate(move): returns move type {pawn, piece, castle, invalid}

def action():
    choice = input('login? : ')
    if(choice == 'y'):
        login()
    game = input('enter game format : ')
    create_game(game)
    time.sleep(5)

    while(1):
        # raw_move = input('next move : ')
        #speak('what is your next move?')
        print('next move : ')
        raw_move = my_word()
        if raw_move == 'stop':
            exit()
        move = transform(raw_move)
        type = validate(move)
        if type != 'invalid':
            print('move is : ',move)
            make_move(move)
        else:
            print('invalid move : ',move)
    
if __name__ == "__main__":
    action()
