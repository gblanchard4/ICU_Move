# Batch create users

from django.contrib.auth.models import UserManager
import argparse

__author__ = "Gene Blanchard"
__email__ = "me@geneblanchard.com"

'''
Create Django Users from a spreadsheet
'''

def main():
	#  Argument Parser
	parser = argparse.ArgumentParser(description='Create Django Users from a spreadsheet')

	# Input file
	parser.add_argument('-i','--input',dest='input', help='The username spreadsheet')
	
	# Parse arguments
	args = parser.parse_args()
	infile = args.input
	
	# Do stuff here 
	with open(infile, 'r') as users:
		for line in users:
			username, email, password = line.rstrip('\n').split('\t')

if __name__ == '__main__':
	main()