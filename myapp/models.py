from email.policy import default
from secrets import choice
from turtle import position
from django.db import models
from django.utils import timezone


	


# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	address=models.TextField()
	city=models.CharField(max_length=100)
	zipcode=models.PositiveIntegerField()
	mobile=models.PositiveIntegerField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to="profile_pic/")
	

	def __str__(self):
		return self.fname+" "+self.lname

class Signup(models.Model):

	status = (
	("Entry" , "Entry"),
	("Exit" , "Exit"),
	)

	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	gender=models.CharField(max_length=100)
	cname=models.CharField(max_length=100)
	purpose=models.CharField(max_length=100)
	tosee=models.CharField(max_length=100)
	todepartment=models.CharField(max_length=100)
	date=models.DateTimeField(default=timezone.now)
	made_on = models.DateTimeField(auto_now_add=True)
	current_status = models.CharField(max_length=10, choices=status , default="Entry")
	

	def __str__(self):
		return self.fname+" "+self.lname