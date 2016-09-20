import csv
import random
import pandas as pd


###optional, either write 10000 a time or 1000000 a time (try to make good use of cpu an io)

class genbigdata:
    chlases = ["class"+str(i) for i in range(20)]
    userId = ["Y00"+str(i) for i in range(500)]


    """docstring for genbigdata"""
    def __init__(self, filename, chunk_size, iter_time):
        self.filename = filename
        self.chunk_size = chunk_size
        self.iter_time = iter_time

    def pdtocsv(self):
        outfile = open(self.filename, "a")
        # headers : ["class","userId","index_id"]
        for x in range(self.iter_time):
            print("itering time %d....."%x)
            #prepare data
            gendata = genbigdata.prepchunk(self.chunk_size)
            gendata.to_csv(outfile, index=False,header=False)
        outfile.close()

    @staticmethod
    def prepchunk(chunk_size):
        data = {
        "class":[random.choice(genbigdata.chlases) for x in range(chunk_size)],
        "userId":[random.choice(genbigdata.userId) for x in range(chunk_size)],
        "index_id":[str(chunk_size)+str(x) for x in range(chunk_size)]
        }
        return pd.DataFrame(data)


if __name__ == '__main__':
    runing = genbigdata("pdbig.csv", 40000, 25000)
    runing.pdtocsv()
