
def gettalk(type='shout'):
    def whisper(word='da'):
        return word.lower()+ '.....'
    def shout(word = 'da'):
        return word.upper() + '!'

    if type == 'shout':
        return shout
    else:
        return whisper

talk = gettalk()
print(gettalk('whisper')())


