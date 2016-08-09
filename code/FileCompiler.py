"""
This file includes modules to compile programs based on different programming language.
Author: Jingran Xue
Email: rannie.xue@gmail.com
"""

import Database
import FileSystem
import os

from subprocess import call


def cProgram(path, filename, para):
	#compile into executable file
	#file = ''.join(path, CFileName)
	file = str(path) + str(filename)
	print file
	fileToExecute = file[:-2]	
	call(['gcc','-Wall', file,'-o',fileToExecute])
	#print fileToExecute
	#run excecutable file
	result = call([fileToExecute, para])

def cplusProgram(path, filename, para):
	pass

def javaProgram(path, filename, para):
	file = str(path) + str(filename)
	print file
	fileToExecute = file[:-5]	
	call(['javac', file])
	print fileToExecute
	result = call(['java', fileToExecute, para])


def pythonProgram(path, filename, para):
	file = str(path) + str(filename)
	print file
	call(['python', file, para])


if __name__== '__main__':
	path = "/Users/Jingran/StudentGradingSystem/code/TestCode/"
	
	CFileName = "CTestCode.c"
	CPara = 'This is a C test code. You made it!'
	cProgram(path, CFileName, CPara)

	JavaFileName = "JavaTestCode.java"
	JPara = "This is a Java test code. You made it!"
	javaProgram(path, JavaFileName, JPara)

	PyFileName = "PyTestCode.py"
	PPara = 'This is a python test code. You made it!'
	pythonProgram(path, PyFileName, PPara)

