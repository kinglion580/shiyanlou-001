#coding:utf-8
"""train ticket

Usage:
	tickets [-gdtkz] <from> <to> <date>

Options:
	-h,--help	show help
	-g		gaotie
	-d		dongche
	-t		tekuai
	-k		kuaisu
	-z		zhida

Example:
	tickets beijing shanghai 2016-10-10
	tickets -dg chengdu nanjing 2016-10-10
"""
from docopt import docopt
from stations import stations
import requests

def cli():
	"""command-line interface"""
	arguments=docopt(__doc__)
	from_station = stations.get(arguments['<from>'])
	to_station = stations.get(arguments['<to>'])
	date = arguments['<date>']

	url='https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,from_station,to_station)
	#print(url)
	r=requests.get(url,verify=False)
	print(r.text)
	#print(r.json())
if __name__=='__main__':
	cli()

