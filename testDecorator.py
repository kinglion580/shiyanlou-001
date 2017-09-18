#!/usr/bin/env python3

from datetime import datetime

def log(func):
	def decorator(*args):
		print('Function '+func.__name__+' has been called at '+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		return func(*args)
	return decorator


@log
def add(x,y):
	return x+y

@log 
def cut(x,y):
	return x-y

@log
def show():
	return "hello shiyanlou"


if __name__=="__main__":
	add(1,2)
	cut(5,3)
	show()
