def shout(word="да"):
    return word.capitalize() + "!"


scream = shout

# def gettalk(type='shout'):
#     def whisper(word='da'):
#         return word.lower()+ '.....'
#     def shout(word = 'da'):
#         return word.upper() + '!'
#
#     if type == 'shout':
#         return shout
#     else:
#         return whisper
#
#
# talk = gettalk()
# print(talk())
# print(gettalk('whisper')())


def doSometheingBefore(func):
    print('do something before function')
    print (func())
doSometheingBefore(scream)