import pickle


def bf_append():
    f = open("D:/sports.dat", "ab")

    data_log = []

    print("Append Data")

    pcode = int(input("Enter the Player code:"))
    pname = input("Enter Player Name:")
    score = int(input("Enter individual score:"))
    rank = int(input("Enter Player Rank:"))

    data_log.append([pcode, pname, score, rank])

    pickle.dump(data_log, f)
    f.close()


bf_append()
