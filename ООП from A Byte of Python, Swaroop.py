# A Byte of Python , Версия 2.01
# Глава 14. Объектно-ориентированное программирование


class Robot:
    '''Представляет робота с именем.'''
    # Переменная класса, содержащая количество роботов
    population = 0
    def __init__(self, name):
        '''Инициализация данных.'''
        self.n = name
        print('(Инициализация {0})'.format(self.n))
        # При создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.population += 1
    def __del__(self):
        '''Я умираю.'''
        print('{0} уничтожается!'.format(self.n))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} был последним.'.format(self.n))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))
    def sayHi(self):
        '''Приветствие робота.
        Да, они это могут.'''
        print('Приветствую! Мои хозяева называют меня {0}.'.format(self.n))
    def howMany():
        '''Выводит численность роботов.'''
        print('У нас {0:d} роботов.'.format(Robot.population))
    howMany = staticmethod(howMany)
droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()
print("\nЗдесь роботы могут проделать какую-то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2

Robot.howMany()

''' Вывод:
$ python3 objvar.py
(Инициализация R2-D2)
Приветствую! Мои хозяева называют меня R2-D2.
У нас 1 роботов.
(Инициализация C-3PO)
Приветствую! Мои хозяева называют меня C-3PO.
У нас 2 роботов.
Здесь роботы могут проделать какую-то работу.
Роботы закончили свою работу. Давайте уничтожим их.
R2-D2 уничтожается!
Осталось 1 работающих роботов.
C-3PO уничтожается!
C-3PO был последним.
У нас 0 роботов.'''
