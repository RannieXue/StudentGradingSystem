"""
This file includes modules to compile programs based on different programming language.
Author: Jingran Xue
Email: rannie.xue@gmail.com
"""

import Database
import FileSystem
import os
import sys

from subprocess import call, check_output, Popen, PIPE, check_call


def cProgram(path, filename, para):
	#compile into executable file
	#file = ''.join(path, CFileName)
	file = str(path) + str(filename)
	print file
	fileToExecute = file[:-2]	
	call(['gcc','-Wall', file,'-o',fileToExecute])
	#print fileToExecute
	#run excecutable file
	result = check_output([fileToExecute, para])
	return result

def cplusProgram(path, filename, para):
	pass

def javaProgram(path, filename, para):
	file = str(path) + str(filename)
	print file
	fileToExecute = filename[:-5]	
	call(['javac', file])
	#print fileToExecute

	#result = check_output(['cd', path, '; java ', fileToExecute, para])
	#result = check_output(['java ', fileToExecute, para])
	#p = Popen(['cd', path, '; java ', fileToExecute, para], stdout = PIPE, stderr = PIPE)
	#output, err = p.communicate(b"input data that is passed to subprocess' stdin")
	#result = p.returncode

	java_class,ext = os.path.splitext(file)
	cmd = ['cd', path, '; java ', fileToExecute, para]
	p= Popen(cmd, shell=True, stdout=PIPE, stderr = PIPE)

	output, err = p.communicate()

	#return check_call(cmd, shell=True)
	return output, err

def pythonProgram(path, filename, para):
	file = str(path) + str(filename)
	print file
	result = check_output(['python', file, para])
	return result

if __name__== '__main__':
	path = "/Users/Jingran/StudentGradingSystem/code/TestCode/"
	
	CFileName = "CTestCode.c"
	CPara = 'This is a C test code. You made it!'
	#print cProgram(path, CFileName, CPara)

	JavaFileName = "JavaTestCode.java"
	JPara = "This is a Java test code. You made it!"
	print javaProgram(path, JavaFileName, JPara)

	PyFileName = "PyTestCode.py"
	PPara = 'This is a python test code. You made it!'
	#print pythonProgram(path, PyFileName, PPara)

