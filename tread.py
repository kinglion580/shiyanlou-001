import os

from multiprocessing import Process

def hello(name):
	print('child process:{}'.format(os.getpid()))
	print('hello'+name)

def main():
	p=Process(target=hello,args=('shiyanlou',))
	#p=Process(hello('shiyanlou'))
	p.start()
	p.join()
	print('parent process: {}'.format(os.getpid()))

if __name__=='__main__':
	main()

