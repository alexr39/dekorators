# def shout(word="да"):
#     return word.capitalize() + "!"
#

# scream = shout

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


# def dosomethingbefore(func):
#     print('do something before function')
#     print (func())


# dosomethingbefore(scream)

def my_new_dekorator(a_function_to_decorate):
    def the_wrapper_arround_original_function():
        print('This is code before original function running\n')
        a_function_to_decorate()
        print('This is code after original function\n')

    return the_wrapper_arround_original_function()

@my_new_dekorator
def a_stand_alone_function():
    print('Just a simple function, please dont change me!\n')


# a_stand_alone_function()

a_stand_alone_function
