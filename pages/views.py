from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail

from solutions.models import *
from contact.models import *

from contact.forms import *

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

class ContactView(View):
	template_name = 'contact.html'

	def get(self, request):
		form = ContactUsForm()

		context = {
			'form': form,
		}

		return render(request, self.template_name, context)

	def post(self, request):
		form = ContactUsForm(request.POST)

		if request.method == 'POST':
			if form.is_valid():
				form.save()
				subject = 'Contact Us'
				body = {
					'first_name': form.cleaned_data['first_name'], 
	                'last_name': form.cleaned_data['last_name'], 
	                'email': form.cleaned_data['email'], 
	                'details': form.cleaned_data['details'],
				}
				message = "\n".join(body.values())
				send_mail(subject, message, 'eavhshelumiel@gmail.com', ['eavshelumiel@gmail.com'])
				form = ContactUsForm()
			else:
				form = ContactUsForm()
		else:
			form = ContactUsForm()

		context = {
			'form': form,
		}

		return redirect(thanks)

def thanks(request):
	template = 'thanks.html'
	context = {}

	return render(request, template, context)
