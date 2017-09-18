#!/usr/bin/env python3

def fib(n):
	print(n)
	current=0
	print("current=",current)
	a,b=1,1
	print("a=",a,"b=",b)
	while current<n:
		print("-------------------")
		yield a
		a,b=b,a+b
		current+=1
		print("a=",a,"b=",b,"current",current)

if __name__=="__main__":
	f5=fib(5)
	print("==========================")
	for x in f5:
		print(x)

