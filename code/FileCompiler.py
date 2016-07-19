"""
This file includes modules to compile programs based on different programming language.
Author: Jingran Xue
Email: rannie.xue@gmail.com
"""

import Database
import FileSystem

from subprocess import call

class FileCompiler(object):
	def cProgram(location, CFileName, args):
		#compile into executable file
		file = ''.join(location, CFileName)
		fileToExecute = file[:-2]
		print(fileToExecute)		
		call(['gcc','-Wall', CFileName,'-o',fileToExecute])

		#run excecutable file
		result = call([fileToExecute, input])


	def cplusProgram():
		pass


	def javaProgram():
		pass


	def pythonProgram():
		pass

location = "/Users/Jingran/StudentGradingSystem/code/TestCode"
CFileName = "CTestCode.c"
FileCompiler().cProgram(location,CFileName)
