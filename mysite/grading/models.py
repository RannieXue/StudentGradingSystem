from django.db import models

class Submission(models.Model):
	student_name = models.CharField(max_length = 140)
	student_id = models.CharField(max_length = 10)
	student_email = models.EmailField()

	course = models.CharField(max_length = 50)
	assignment = models.CharField(max_length = 50)	

	date = models.DateTimeField()
	file_title = models.CharField(max_length = 140)
	file_type = models.CharField(max_length = 50)
	file_content = models.FileField()
	file_version = models.CharField(max_length = 10)

	grade = models.IntegerField()

	def __str__(self):
		return self.file_title



