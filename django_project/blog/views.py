from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
	{
		'author':'coreyms',
		'title':'Blog',
		'content':'First post',
		'data_posted':'August 27,2019'
	},
	{
		'author':'Jane Doe',
		'title':'Blog 2',
		'content':'Second post',
		'data_posted':'June 27,2019'
	}
]

def home(request):
	context = {
		'posts':posts
	}
	return  render(request,'blog/home.html',context)

def about(request):
	return  render(request,'blog/About.html',{'title' : 'About'})