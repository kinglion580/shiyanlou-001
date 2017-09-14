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
def cli():
	"""command-line interface"""
	arguments=docopt(__doc__)
	print(arguments)

if __name__=='__main__':
	cli()

