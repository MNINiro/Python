import pickle

def storeData():
    # initializing data to be stored in db
    Omar = {'key': 'Omar', 'name': 'Ayman Ahmed','age': 28, 'pay': 40000}
    Shabab = {'key': 'Shabab', 'name': 'Shabab Ahmed','age': 25, 'pay': 50000}

    # database
    db = {}
    db['Omar'] = Omar
    db['Shabab'] = Shabab

    # Its important to use binary mode
    dbfile = open('D:/examplePickle.dat', 'ab')

    # source, destination
    pickle.dump(db, dbfile)
    dbfile.close()


def loadData():
    # for reading also binary mode is important
    dbfile = open('D:/examplePickle.dat', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()


if __name__ == '__main__':
    storeData()
    loadData()