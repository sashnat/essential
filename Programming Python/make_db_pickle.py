# В примере 1.5 демонстрируется, как с помощью
# модуля pickle можно сохранять записи в файле.
from initdata import db
import pickle
dbfile = open('people-pickle', 'wb') # в версии 3.X следует использовать
pickle.dump(db, dbfile) # # записывает сериализованный объект в файл
dbfile.close() # данные имеют тип bytes, а не str
