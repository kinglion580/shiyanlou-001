from multiprocessing import Pipe,Process

conn1,conn2=Pipe()

def f1():
	conn1.send('Hello shiyanlou')
	conn1.send('Hello shiyanlou2')
	conn1.send('Hello shiyanlou3')

def f2():
	data=conn2.recv()
	data2=conn2.recv()
	print(data,data2)

def main():
	Process(target=f1).start()
	Process(target=f2).start()

if __name__=='__main__':
	main()
