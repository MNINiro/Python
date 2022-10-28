def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(fun):
    # storing the function in a variable
    greeting = fun("Hi, I am created by a function passed as an argument.")
    print(greeting)


greet(shout)
greet(whisper)
