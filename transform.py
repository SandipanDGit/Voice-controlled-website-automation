#TRANSFORM INTO ALGEBRIC NOTATION

def transform(text):
    if text is None:
        print('bad input in transform')
        return None
    text = text.lower().strip()
    move = ''
    text = text.replace('king','K')
    text = text.replace('queen','Q')
    text = text.replace('rook','R')
    text = text.replace('bishop','B')
    text = text.replace('night','N')
    text = text.replace('knight','N')
    text = text.replace('pawn','')
    text = text.replace('takes','x')
    text = text.replace('text','x')
    text = text.replace('captures','x')
    text = text.replace('to','2')
    text = text.replace('check','+')
    text = text.replace('mate','#')
    text = text.replace('+#','#')
    text = text.replace('promotes','=')
    text = text.replace('one','1')
    text = text.replace('two','2')
    text = text.replace('three','3')
    text = text.replace('four','4')
    text = text.replace('five','5')
    text = text.replace('six','6')
    text = text.replace('seven','7')
    text = text.replace('eight','8')
    text = text.replace('short castle','O-O')
    text = text.replace('long castle','O-O-O')
    text = text.replace('see','c')
    text = text.replace('before','b4')
    text = text.replace('jeetu','g2')

    parts = text.split(' ')
    for part in parts:
        move = move + part
    return move

if __name__ == "__main__":
    text = input('input raw move in english : ')
    move = transform(text)
    print(move)
