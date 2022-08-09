from django.db import models

# Create your models here.

solution_type = (
		('Home', 'Home'),
		('Normal', 'Normal'),
	)

solution_category = (
		('Network', 'Network'),
		('Digital Marketing ', 'Digital Marketing '),
		('Data Science & Analytics', 'Data Science & Analytics')
	)


class Solution(models.Model):
	name = models.CharField(max_length=9999)
	desc = models.TextField()
	img = models.ImageField(upload_to='solutions/img/')
	solution_type = models.CharField(max_length=9999, choices=solution_type, default='Normal')	
	solution_category = models.CharField(max_length=9999, choices=solution_category, default='Network')

	def __str__(self):
		return self.name + ' ' + self.solution_category + ' ' + self.solution_type
