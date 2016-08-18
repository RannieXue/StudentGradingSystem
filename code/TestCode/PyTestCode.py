# This is the test code for pyprogram function
import sys

try:
	first_arg = sys.argv[1]
except IndexError:
	first_arg = ""
	print ("Couldn't read your input.")

def PyTestCode(para = first_arg):
	if len(para)>1:
		print (para)
	else:
		print ("But it still works!")

if __name__=="__main__":
	PyTestCode()