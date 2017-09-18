from multiprocessing import Queue,Process

queue,queue2=Queue()

def f1():
	queue.put('Hello shiyanlou')
	#conn1.send('Hello shiyanlou')
	queue2.put('Hello shiyanlou2')
	#queue.put('Hello shiyanlou3')

def f2():
	data=queue.get()
	data2=queue2.get()
	#data=conn2.recv()
	#data=conn2.recv()
	print(data)

def main():
	Process(target=f1).start()
	Process(target=f2).start()

if __name__=='__main__':
	main()
