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

# def my_new_dekorator(a_function_to_decorate):
#     def the_wrapper_arround_original_function():
#         print('This is code before original function running\n')
#         a_function_to_decorate()
#         print('This is code after original function\n')
#
#     return the_wrapper_arround_original_function()
#
# @my_new_dekorator
# def a_stand_alone_function():
#     print('Just a simple function, please dont change me!\n')
#
#
# # a_stand_alone_function()
#
# a_stand_alone_function

#
# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print('Lets see what i have here:', arg1, arg2)
#         function_to_decorate(arg1, arg2)
#     return a_wrapper_accepting_arguments
#
#
# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print('My name is {} and last name is {}'.format(first_name, last_name))
#
#
# print_full_name('Jakov', 'Melman')


def method_friendly_dekorator(method_to_decorate):
    def wrapper(self, lie):
        lie -= 3
        return method_to_decorate(self, lie)
    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_dekorator
    def sayyourage(self, lie):
        print('I\'m {}, but what do you think, how old am I?'.format(self.age + lie))


l = Lucy()
l.sayyourage(-3)
