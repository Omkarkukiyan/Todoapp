from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model): # The Category table name that inherits models.Model
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name = ("Category")
		verbose_name_plural = ("Categories")

	def __str__(self):
		return self.name

class TodoList(models.Model): #Todolist able name that inherits models.Model
	title = models.CharField(max_length=250)
	content = models.TextField(blank=True)
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
	due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
	category = models.ForeignKey(Category, default="general",  on_delete=models.CASCADE) # a foreignkey

	class Meta:
		ordering = ["-created"] #ordering by the created field

	def __str__(self):
		return self.title