fl2s30time = [8,9,10,11,12,13,14,15,16,17,18]
fl2s30min = [0,0,0,0,0,0,0,0,0,0]

fl2s60time = [800,930,1100,1230,1400,1530]
fl2s60min = [0,0,0,0,0,0,0]

flTime = int(input('Enter flight time:'))
print(fl2s30time.index(flTime))

print(fl2s30min.index(flTime))
