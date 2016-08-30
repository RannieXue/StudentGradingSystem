"""This file is to read test case file and pick 10 test cases randomly. Return a list."""
import random


def Test_picker(file, num):
	#Read file
	with open(file) as f:
		lines = f.read().splitlines()

	length = len(lines)
	#print length

	try:
		index = random.sample(range(1, length-1), num)
	except ValueError:
		print("Sample size exceeded population size.")
	#print index.sort()

	testCase = [lines[i] for i in index]
	#print testCase
	return index, testCase

def Ans_picker(file, index):
	with open(file) as f:
		lines = f.read().splitlines()
	length = len(lines)

	if length > max(index):
		ans = [lines[i] for i in index]
		return ans
	else: 
		print("Answer file length does not match testcase file.")
		return False



print Test_picker('/Users/Jingran/StudentGradingSystem/code/TestCases.txt', 6)

