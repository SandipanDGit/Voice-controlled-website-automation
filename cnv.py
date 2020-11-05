#CHECK IF MOVE IS IN STANDARD ALGEBRIC NOTATION

import re
def validate(move):
    if move is None: 
        print('bad input at validate')
        return 'invalid'
    pawn = re.compile('[a-h](x[a-h])?[1-8](=[QNBR])?(\\+|#)?')
    piece = re.compile('[KQRBN]([a-h][1-8]?)?x?[a-h][1-8](\\+|#)?')
    castle = re.compile('O-O|O-O-O')

    pawn_move = pawn.match(move)
    piece_move = piece.match(move)
    castle_move = castle.match(move)

    if pawn_move is not None:
        return 'pawn'
    elif piece_move is not None:
        return 'piece'
    elif castle_move is not None:
        return 'castle'
    else:
        return 'invalid'

if __name__ == "__main__":
    move = input('enter move : ')
    move_type = validate(move)
    print(move_type)
