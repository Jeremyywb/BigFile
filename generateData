##write 100,000,000 data

import csv
import random


###optional, either write 10000 a time or 1000000 a time (try to make good use of cpu an io)
def createRDdic(i,areas,ids):
    data = []
    for x in range(100000):
        data.append({'ClickID':str(i)+str(x), 
             'userid':random.choice(ids), 
               'area':random.choice(areas)})

    return data


def writeDicRows(i,areas,ids,f_csv):
    data = createRDdic(i,areas,ids)
    f_csv.writerows(data)


def ProcWrite(n):##n=10000
    areas =["area"+str(x) for x in range(200)]
    ids = ["S0"+str(x+1) for x in range(1000)]
    headers = ['ClickID', 'userid', 'area']
    f = open('Bigdata2.csv','w')
    f_csv = csv.DictWriter(f, headers,lineterminator='\n')
    f_csv.writeheader()
    for i in range(n):
        print("trying %d time writing..."%(i+1))
        writeDicRows(i,areas,ids,f_csv)
    f.close()

if __name__ == '__main__':
    ProcWrite(10000)
