###代码分析：

> 项目目标：统计文件的ID频率并从达到小排序
> 项目对象：三个字段，classes（去重200个），userid（去重1000个），clickID（唯一标识）
> 

 1. 生成10亿条随机ID记录

>代码总共用了两种方法。一种使用pandas原生csv包，一种是pandas；当然两种方法写入数据都考虑两个问题。①能够生成数据并往以有的文件**追加**数据，注意是追加不是修改 ②控制内存，分块写入数据，基于这两个考量，两者方案如下

>|**CSV形式**：
> 
>1、使用dic(python字典作为子元素)作为行写入标记，每个dic多个字段（为字典的index）
>2、循环10000次生成一个由10000(记为m)个dic的列表list，接着采用writerows方法将数据写入csv
>调用writerows 100000(记为n)次，这样总共有m*n行写入csv也即10亿条记录
>
>|**pandas写入**
>
>pandas的方法则较为简单，同上，先生成方块的dataframe，然后记住打开文件的时候用append 也即 "a"的方式即可
>




----------


   
 - 分块读取数据并统计相关数据

> |**读取数据的伪代码**
> 
> 主要思想要是分块读取统计，伪代码如下
>1- 读取数据，设置读取对象（文件）方式为可迭代，每次N行，
>2-开始读取，读取N行并获得对象为M
>3-获取对家并处理对象获得相关统计值
>4-迭代，读取第二个N行并统计相关数据，然后更新第三个步骤的统计值

>|**代码讲解**
>
>本项目使用的是pandas，块读取比较简单，参看代码
>统计方式采用pandas的Series方法，每得到一个Dataframe块，获取其要统计的列，也即本项目目标统计ID频率，并声称以ID为为INDEX以统计数为values的Series
>此处统计可能有点难懂，这里使用的是Series的add方法，新生成的对象的ID如果存在在旧的（上次生成的）数据中，那么将旧值更新（那个ID的value加上新对象相同ID的value）
>这里因为每次新的chunk块都是赋值给同一个变量，因此内存上得到一个很好的控制

 - 下面是read数据的时候的尝试log，以及一些备注的链接（还没来得及整理大家可以看看），这里面有使用原生python的文件read的方法，用的是buffring按照bite读取，因为是结构化数据，所以这种方式可能存在行读取不完整，也即存在于两个块的情形，读者可以将方法改成readlines（BUFSIZE=102400）的方案尝试

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
