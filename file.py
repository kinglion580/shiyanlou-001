import sys
import csv

args=sys.argv[1:]
index=args.index('bb')
a=args[index+1]
print("args=",args,"index=",index,"a=",a)


config={}
with open('config.csv') as f:
	for line in f.readlines():
		key,value=line.strip().split('=')
		config[key]=float(value)
	print(config)

userdata_string=[]
userdata_int=[]
with open('userdata.csv') as f:
	for line in f.readlines():
		id,income=line.strip().split(',')
		userdata_string.append(income)
		userdata_int.append(int(income))
	print(userdata_string)
	print(userdata_int)
	print((userdata_int))

a='hello'
b='world'
userdata_int+=[a,b]
print("after change",userdata_int)

with open('result.csv','w') as f:
	writer=csv.writer(f)
	writer.writerows(str(userdata_int))


class A(object):
	def foo1(self):
		print ("method-hello",self)
	
	@staticmethod
	def foo2():
		print ("staticmethod-hello")

	@classmethod
	def foo3(cls):
		print ("classmethod-hello",cls)
	
	
	def writefile(self):
		userdata=[]
		userdata.append(userdata_int)
		with open('result2.csv','w',newline='') as f:
			writer=csv.writer(f)
			writer.writerows(userdata)

	def writefile2(self):
		with open('result3.csv','w',newline='') as f:
			writer=csv.writer(f)
			writer.writerows(userdata_string)

	def writefile3(self):
		with open('result4.csv','w',newline='') as f:
			writer=csv.writer(f)
			writer.writerows([userdata_int])

if __name__=='__main__':

	a=A()
	a.foo1()
	A.foo1(a)

	A.foo2()
	A.foo3()
	print(A)

	a.writefile()
	a.writefile2()
	a.writefile3()

