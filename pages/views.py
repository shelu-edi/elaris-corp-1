from django.shortcuts import render
from django.views import View

from solutions.models import *

# Create your views here.


class HomeView(View):
	template_name = 'index.html'
	queryset = Solution.objects.all()

	def get_queryset(self):
		return self.queryset

	def get(self, request):
		context = {
		'solutions': self.get_queryset(),
		}

		return render(request, self.template_name, context)

class SolutionView(View):
	template_name = 'solutions.html'
	queryset = Solution.objects.all()

	def get_queryset(self):
		return self.queryset

	def get(self, request):
		context = {
		'solutions': self.get_queryset(),
		}

		return render(request, self.template_name, context)

def about(request):
	template = 'about.html'
	context = {}

	return render(request, template, context)
