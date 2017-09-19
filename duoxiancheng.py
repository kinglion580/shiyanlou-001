import threading

def hello(name):
	print('child process:{}'.format(threading.get_ident()))
	print('hello'+name)

def main():
	p=threading.Thread(target=hello,args=('shiyanlou',))
	#p=Process(hello('shiyanlou'))
	p.start()
	p.join()
	print('parent process: {}'.format(threading.get_ident()))

if __name__=='__main__':
	main()

