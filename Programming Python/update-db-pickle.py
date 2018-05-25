# Внесение изменений в базу данных, сохраненную с помощью модуля
# pickle, выполняется точно так же, как и при использовании текстового
# файла, созданного вручную, за исключением того, что все необходимые
# преобразования выполняются стандартным модулем. Как это делает-
# ся, демонстрирует пример 1.7.
import pickle
dbfile = open('people-pickle', 'rb')
# реализовать доступ к сохраненной базе данных после ее создания
# rb - means "open for reading and writing and open in binary mode".
db = pickle.load(dbfile) # загружает объект из файла.
print ("load", db)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom T'

dbfile = open('people-pickle', 'wb')
# сохранять записи в файле, 'wb' - means "open for writing and open in binary mode".
pickle.dump(db, dbfile) # записывает сериализованный объект в файл
print('save', db)
dbfile.close()
