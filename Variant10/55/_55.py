waveLength = int(input("input wave length:"))
if waveLength>=380 and waveLength<450:
    print("fioletovy")
elif waveLength>=450 and waveLength<495:
    print("siny")
elif waveLength>=495 and waveLength<570:
    print("zelyony")
elif waveLength>=570 and waveLength<590:
    print("zhelty")
elif waveLength>=590 and waveLength<620:
    print("orangevy")
elif waveLength>=620 and waveLength<+750:
    print("krasny")
else :
    print("unknow length")