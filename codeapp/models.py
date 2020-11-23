from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse 
from ckeditor.fields import RichTextField

# Create your models here.
class Python(models.Model):
	title = models.CharField(max_length=200)
	content = RichTextField(blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField()
	likes = models.ManyToManyField(User, related_name='blog_pythons')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title 

