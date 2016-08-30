from datetime import datetime
import TestCasePicker
import FileCompiler as fc

def grade(path, file, type, testcase, answerfile, num, due, submit_time):
	score, failed = judge(path, file, type, testcase, answerfile, num)

	time_fmt = ""
	due = datetime.strptime(due, time_fmt)
	submit_time = datetime.strptime(submit_time, time_fmt)

	time_diff = (submit_time - due).days

	if time_diff > 0:
		score -= 0.1 * time_diff * score

	return score




def judge(path, file, type, testcase, answerfile, num):
	
	indx, test_lst = TestCasePicker.Text_picker(testcase, num)
	ans_lst = TestCasePicker.Ans_picker(answerfile,indx)
	
	count = 0
	failed = []

	for index, test in enumerate(test_lst):
		try:
			if type == 'C':
				rst = fc.cProgram(path, file, test)
			elif type == 'C++':
				rst = fc.cplusProgram(path, file, test)
			elif type == 'Java':
				rst = fc.javaProgram(path, file, test)
			elif type == 'Python':
				rst = fc.pProgram(path, file, test)
			else:
				print "Unrecognized File type: ", type
				break

			if rst == ans_lst[index]:
				count += 1
			else:
				failed.append(test)
		except:
			print "There's an error while running testcase: ", test

	score = int(count/num *100)
	return score, failed
