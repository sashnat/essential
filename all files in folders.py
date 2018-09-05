import os
tree = os.walk('Z:\Python')
print(tree)

pdir = 'Z:\Python'
contdir = []
for i in os.walk(pdir):
    contdir.append(i)

for i in contdir:
    print (i)

for d, dirs, files in os.walk('Z:\Python'):
    for f in files:
        print (f)
'''Для получения полных адресов подойдет функция 
os.path.join(). С ее помощью можно объединить первый элемент кортежа, содержащий полный 
путь, с именем каждого файла:'''
path_f = []
for d, dirs, files in os.walk('Z:\Python'):
    for f in files:
        path = os.path.join(d,f) # формирование адреса
        path_f.append(path) # добавление адреса в список
print(path_f )


# получить полный путь для каждого файла с новой строки
print('\n'.join(i for i in path_f))
#it's another way to get the same result
for i in path_f:
    print(i, end='\n')
