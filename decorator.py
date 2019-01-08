# https://habr.com/post/141411/

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


# --------с помощью декоратора-------------------
@makebold
@makeitalic
def hello():
    return "hello habr"

print (hello()) ## выведет <b><i>hello habr</i></b>


# --------без декоратора-------------------
def hello1():
    return "hello habr"

wer = makebold(hello1)
print (wer())          # выведет <b>hello habr</b>

'''
def поведение(x):
   def механизм:
     .....
    return механизм

def функция:

результат = поведение(функция)
'''
