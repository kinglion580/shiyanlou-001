import time
from multiprocessing import Process,Value,Lock

def func(val,lock):
	for i in range(50):
		time.sleep(0.01)
		with lock:
			val.value+=1

		#lock.acquire()
		#val.calue+=1
		#lock.release()

if __name__=='__main__':
	v=Value('i',0)
	lock=Lock()
	procs=[Process(target=func,args=(v,lock)) for i in range(10)]
	
	for p in procs:
		p.start()
	for p in procs:
		p.join()

	print(v.value)
