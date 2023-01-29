# create the wordTable containing valid two-letter words and their points values
wordTable = [["aa", 2], ["ab", 4], ["ad", 2], ["ae", 1], ["ag", 3], ["ah", 4], ["ai", 2], ["al", 2], ["am", 3],
             ["an", 2],
             ["ar", 2], ["as", 1], ["at", 2], ["aw", 4], ["ax", 8], ["ay", 3], ["ba", 4], ["be", 2], ["bi", 3],
             ["bo", 4],
             ["by", 8], ["da", 2], ["de", 2], ["di", 2], ["do", 2], ["ed", 2], ["ef", 8], ["eh", 4], ["el", 4],
             ["em", 4],
             ["en", 2], ["er", 2], ["es", 2], ["et", 2], ["ex", 8], ["fa", 4], ["fe", 4], ["fi", 4], ["fo", 4],
             ["fy", 10],
             ["gi", 4], ["go", 3], ["ha", 4], ["he", 2], ["hi", 2], ["ho", 4], ["id", 4], ["if", 4], ["in", 2],
             ["is", 2],
             ["it", 2], ["jo", 10], ["ka", 8], ["ki", 5], ["la", 2], ["li", 2], ["lo", 2], ["ma", 3], ["me", 2],
             ["mi", 2],
             ["mo", 3], ["mu", 4], ["my", 8], ["na", 2], ["ne", 2], ["no", 2], ["nu", 4], ["od", 4], ["oe", 4],
             ["of", 4],
             ["oh", 4], ["oi", 2], ["ok", 8], ["om", 4], ["on", 2], ["op", 4], ["or", 2], ["os", 4], ["ow", 4],
             ["ox", 8],
             ["oy", 8], ["pa", 4], ["pe", 2], ["pi", 3], ["po", 2], ["qi", 10], ["re", 2], ["sh", 4], ["si", 2],
             ["so", 2],
             ["ta", 2], ["te", 2], ["ti", 2], ["to", 2], ["uh", 4], ["um", 4], ["un", 2], ["up", 4], ["us", 2],
             ["ut", 2],
             ["we", 4], ["wo", 4], ["xi", 8], ["xu", 8], ["ya", 3], ["ye", 2], ["yi", 4], ["yo", 4], ["za", 8]]


# function to check if a given two-letter word is valid
def checkWord(word):
    for i in range(len(wordTable)):
        if word == wordTable[i][0]:
            return True
    return False


# test the function
print(checkWord("ab"))  # should return True
print(checkWord("zz"))  # should return False
