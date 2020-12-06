from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse 


# Create your views here.
from .models import Python

def about(request):
	return render(request, 'codeapp/about.html')

def LikeView(request, pk):
	python = get_object_or_404(Python, id=request.POST.get('python_id'))
	python.likes.add(request.user)
	return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

def index(request):
	pythons = Python.objects.all()
	return render(request, 'codeapp/index.html', {'pythons':pythons})

def detail(request, python_id):
	python = get_object_or_404(Python, pk=python_id)
	stuff = get_object_or_404(Python, id=python_id)
	total_likes = stuff.total_likes()
	return render(request, 'codeapp/detail.html', {'python':python, 'total_likes':total_likes})
	