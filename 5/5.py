import pickle


def five():
    reader = pickle.load(open('D:/banner.p', 'rb'))
    print reader

    for i in reader:
        print "".join([x[0] * x[1] for x in i])

five()