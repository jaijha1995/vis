from django.shortcuts import render,redirect
from.models import User,Signup
from django.core.mail import send_mail
from django.http import HttpResponse  
from mysite import settings
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 
# relative import of forms
from .models import Signup
from .forms import SignupForm

# Create your views here.

def index(request):
	try:
		user=User.objects.get(email=request.session['email'])
		return render(request,'in.html')
	except:
		return render(request,'index.html')
	

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(
					email=request.POST['email'],
					password=request.POST['password']

				)
			request.session['email']=user.email
			request.session['fname']=user.fname
			#request.session['profile_pic']=user.profile_pic.url 
			return render(request,'in.html')
		except:
			msg="Email or Password is Incorrect"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		#del request.session['profile_pic']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def signup(request):
	if request.method=="POST":
		Signup.objects.create(
				fname=request.POST['fname'],
				lname=request.POST['lname'],
				#email=request.POST['email'],
				mobile=request.POST['mobile'],
				address=request.POST['address'],
				gender=request.POST['gender'],
				entry=request.POST['entry'],
				cname=request.POST['cname'],
				purpose=request.POST['purpose'],
				tosee=request.POST['tosee'],
				todepartment=request.POST['todepartment'],

					

			)
		msg="Visitor Enrollment Successfully"
		return render(request,'signup.html',{'msg':msg})
		
	else:
		msg=""
		return render(request,'signup.html',{'msg':msg})

def back(request):
	return render(request,'in.html')

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect('logout')
			else:
				msg="New password & Confirm New Password Does Not matched"
				return render(request,'change_password.html',{'msg':msg})
		else:
			msg="Old Password does Not Matched"
			return render(request,'change_password.html',{'msg':msg})

	else:
		return render(request,'change_password.html')

def new_password(request):
	email=request.POST['email']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user=User.objects.get(email=email)
		user.password=np
		user.save()
		msg="Password Updated Successfully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg="New Password & Confirm New Password Does Not Matched"
		return render(request,'new_password.html',{'email':email,'msg':msg})

def photo_capture(request):
	return render(request,'photo_capture.html')

def visitor_view(request):
	if request.method=="POST":
		signups=Signup.objects.all()#.order_by('-id')[:3]
		return render(request,'visitor_view.html' ,{'msg':msg,'signups':signups})
	else:
		signups=Signup.objects.all()#.order_by('-id')[:3]
		return render(request,'visitor_view.html',{'signups':signups})

def visitor_exit(request):
	if request.method=="POST":
		signups=Signup.objects.all()
		return render(request,'visitor_exit.html' ,{'msg':msg,'signups':signups})
	else:
		signups=Signup.objects.all()
		return render(request,'visitor_exit.html',{'signups':signups})


def mail(request):  
    subject = "Greetings"  
    msg     = "Congratulations for your success"  
    to      = "irfan.sssit@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Signup, id = id)
 
    # pass the object as instance in form
    form = SignupForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)


