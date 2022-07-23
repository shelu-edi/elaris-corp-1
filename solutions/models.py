from django.db import models

# Create your models here.

solution_type = (
		('Home', 'Home'),
		('Normal', 'Normal'),
	)

class Solution(models.Model):
	name = models.CharField(max_length=9999)
	desc = models.TextField()
	img = models.ImageField(upload_to='solutions/img/')
	solution_type = models.CharField(max_length=9999, choices=solution_type, default='Normal')	

	def __str__(self):
		return self.name + ' ' + self.solution_type
