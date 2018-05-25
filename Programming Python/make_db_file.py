"""
Save in-memory database object to a file with custom formatting;
assume 'endrec.', 'enddb.', and '=>' are not used in the data;
assume db is dict of dict;  warning: eval can be dangerous - it
runs strings as code;  could also eval() record dict all at once;
could also dbfile.write(key + '\n') vs print(key, file=dbfile);
"""

dbfilename = 'people-file'
ENDDB  = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, x=dbfilename): # sash: можно заменить dbfilename=dbfilename на X=dbfilename
    # sash: Переменной (имени файла) dbfilename присваивается значение dbfilename, которое равно 'people-file' (имя создаваемого файла)
    "formatted dump of database to flat file - сохраняет базу данных в файл"
    dbfile = open(x, 'w') # sash: можно заменить (dbfilename, 'w') на (X, 'w')
    print("формирует файл, пока пустой ?")
    print(1, [key if key in db else 'none' for key in db], file=dbfile)
    for key in db:
        print(key, 111,  file=dbfile) # записывет данные (key) в файл file=dbfile('people-file') c переменной file
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)# repr - представление объекта в виде строки
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    #print(ENDDB, repr("the end"), 'end', file=dbfile) 
    dbfile.close()

def loadDbase(dbfilename=dbfilename):
    print('загрузка базы')
    "parse data to reconstruct database - восстанавливает данные, реконструируя базу данных"
    dbfile = open(dbfilename)
    print('load')
    import sys
    sys.stdin = dbfile # прием данных Кодировка, используем sys.stdin/sys.stdout, чтобы текст в байты превратить и обратно
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value) # преобразовывает строку в код
            field = input()
        db[key] = rec
        key = input()
    return db

#если интерпретатор запускает некоторый модуль (исходный файл) как основную программу,
#он присваивает специальной переменной __name__ значение "__main__".
#Если этот файл импортируется из другого модуля, переменной __name__ будет присвоено имя этого модуля.
if __name__ == '__main__':
    from initdata import db
    print('какая это строка?')
    storeDbase(db)
    print ("самостоятельный сценарий - __name__ == '__main__' - true")

for line in open('people-file'):
    print(line, end='')
