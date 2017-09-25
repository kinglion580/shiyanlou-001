import sys
from getopt import getopt
import configparser

options,_=getopt(sys.argv[1:],'C:c:d:o')
print(options)
options=dict(options)
print(options)

value1=options.get('-C')
print('after -C ',value1)
value2=options.get('-c')
print('after -c ',value2)
value3=options.get('-d')
print('after -d ',value3)
value4=options.get('-o')
print('after -o ',value4)

class A:
	def __init__(self):
		self.config=self._read_config()
	def _read_config(self):
		config=configparser.ConfigParser()
		config.read('config2.cfg')
		for c in config:
			print("config=",c)
		if(value1) and value1.upper() in config.sections():
			print("config[value1.upper()]=",config[value1.upper()])
			return config[value1.upper()]
		else:
			print("default=",config['DEFAULT'])
			return config['DEFAULT']


	def _get_config(self):
		return self.config['JishuL']
a=A()
print(a._get_config())



