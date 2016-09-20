import pandas as pd

chunker = pd.read_csv("Bigdata.csv",iterator=True, chunksize= 100000)
tot = pd.Series([])

i = 0
for piece in chunker:
    i = i+1
    if i>=80:
        print("\n")
        i = 0
    print("#",end='')
    tot = tot.add(piece["userid"].value_counts(), fill_value = 0)
    
tot = tot.order(ascending = False)

print("\n\n\n###############################\n#",
    tot,
    "\n###############################")

chunker.close()
