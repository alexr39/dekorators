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


# def method_friendly_dekorator(method_to_decorate):
#     def wrapper(self, lie):
#         lie -= 3
#         return method_to_decorate(self, lie)
#     return wrapper
#
#
# class Lucy(object):
#
#     def __init__(self):
#         self.age = 32
#
#     @method_friendly_dekorator
#     def sayyourage(self, lie):
#         print('I\'m {}, but what do you think, how old am I?'.format(self.age + lie))
#
#
# l = Lucy()
# l.sayyourage(-3)


# def a_decorator_passing_arbitary_arguments(function_to_decorate):
#     def a_wrapper_accepting_arbitary_arguments(*args, **kwargs):
#         print('Pushed anything to me?:')
#         print(args)
#         print(kwargs)
#         function_to_decorate(*args, **kwargs)
#     return a_wrapper_accepting_arbitary_arguments
#
#
# @a_decorator_passing_arbitary_arguments
# def function_with_no_argument():
#     print('No arguments here')
#
# function_with_no_argument()
#
# @a_decorator_passing_arbitary_arguments
# def function_with_arguments(a,b,c):
#     print(a, b, c)
#
# function_with_arguments(1,2,3)
#
#
# @a_decorator_passing_arbitary_arguments
# def function_with_named_arguments(a, b, c, platypus = 'Why not?'):
#     print('lovely {0} {1} {2}? {3}'.format(a, b, c, platypus))
#
# function_with_named_arguments('Bill', 'Lucy', 'Jack', platypus='Of course!')
#
#
# class Mary(object):
#
#
#     def __init__(self):
#         self.age = 31
#
#     @a_decorator_passing_arbitary_arguments
#     def sayyourname(self, lie = -3):
#         print('I\'m {} yo'.format(self.age + lie))
#
# m = Mary()
# m.sayyourname()


# def my_decorator(func):
#     print("Я обычная функция")
#     def wrapper():
#         print ("Я - функция, возвращаемая декоратором")
#         func()
#     return wrapper
#
#
# def lazy_function():
#     print("zzzzzzzz")
#
# lazy_function = my_decorator(lazy_function)
#
# lazy_function()

# def decorator_maker():
#
#     print('Я создаю декораторы! я буду вызван только РАЗ: ' +\
#           'когда ты попросишь меня создать декоратор')
#
#     def my_decorator(func):
#
#         print('Я - декоратор! я буду вызван только один раз: в момент декорирования функции!')
#
#         def wrapped():
#             print('\nСама обертка декорируемой функции.'
#                   'Будет вызываться каждый раз когда будет использована декорируемая функция'
#                   'Я возвращаю результат работы декорируемой функции')
#             return func()
#
#         print('Я возвращаю обернутую функцию')
#         return wrapped
#
#     print('я возвращаю декоратор')
#     return my_decorator
#
# @decorator_maker()
# def decorated_function():
#     print('\nЯ декорируемая функция\n')
#
#
# decorated_function()


def decorator_maker_with_args(decorator_arg1, decorator_arg2):

    print('I\'m creating docorator! And I recieved following arguments:', decorator_arg1, decorator_arg2)


    def my_decorator(func):
        print('\nThis is decorator and here are arguments',  decorator_arg1, decorator_arg2)

        def wrapper(function_arg1, function_arg2):
            print('I\'m wrapper around original function.\n'
                  'And i have access to all arguments: \n'
                  '\t - decorator arguments: {0} {1} \n'
                  '\t - function arguments: {2} {3}.\n'
                  'Now I can push arguments on'.format(decorator_arg1, decorator_arg2, function_arg1, function_arg2))
            return func(function_arg1, function_arg2)
        return wrapper
    return my_decorator
@decorator_maker_with_args('Leonard', 'Sheldon')
def decorate_function_with_arguments(function_arg1, function_arg2):
    print('I\'m function for decoration and I know only about my arguments {0} and {1}'.format(function_arg1, function_arg2))


decorate_function_with_arguments('Radjesh', 'Hovard')
