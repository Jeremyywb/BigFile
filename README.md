# BigFile
read big file and do some process with it

```
# import csv
#helpful link but not enough: http://chenqx.github.io/2014/10/29/Python-fastest-way-to-read-a-large-file/
#que:require some read whole thing 1G may not macth all,will lead to some left
#after some research read by size mean at least but also read finall left 
#最后剩下的不足指定size则只读取剩下的
#而巨大的问题是读取数据被拆分，不完整的行

##key word 1: buffer
##answer1 : pandas iterate file:
##read by chunk:http://pandas.pydata.org/pandas-docs/stable/io.html#io-chunking
##append and write : http://stackoverflow.com/questions/31090127/pandas-continuously-write-from-function-to-csv


# def read_in_chunks(filepath, chunkszie = 1024*1024 ):
# 	filie_boj = open(filepath)
# 	while  True:
# 		chunkData = filie_boj.read(chunkszie)
# 		if not chunkData:
# 			break
# 		yield chunkData

# def proce(data):
# 	pass

# def writeResult(data):
# 	data.to_csv("answers.csv")

# if __name__ == '__main__':
# 	filepath = "./Bigdata.csv"
# 	temp = pd.Dataframe()
# 	i = 0
# 	for chunk in read_in_chunks(filepath):
# 		i = i+1
# 		print("proced %d data succefully..."%i)
# 		peoced = proce(chunk)
# 		temp.append(peoced)
# 	print(temp)
# 	writeResult(temp)

# ##exmple buffering

# output = open("example.csv",a)

# with open("bigdata.csv", buffering=20000000) as f:
# 	for line in f:
# 		saveLine = line.replace("old", "new")
# 		output.write(saveLine)

# 	output.close()

```
