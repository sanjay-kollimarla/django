from django.shortcuts import render
from django.urls import path,re_path as url
from django.http import HttpResponseRedirect
from task.models import Users_Model,Tasks_Model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
global token,user_id,rc
user_id=''
token=''
rc=False
def login(request):
    global token
    token=''
    user_id=''
    print("nullifying token",token)    
    return render(request,'login.html')
def validate(request):
    global token,user_id
    if request.POST['action'] =='register':
        return HttpResponseRedirect('register')
    token=''
    username,password= request.POST['username'],request.POST['password']
    try:
        
        user=Users_Model.objects.get(username=username)
        token = RefreshToken.for_user(user)
        user_id=user.id
        print("this is user id",user_id)
        if user.password!=password:
            raise
       
       
    except:
        
        return render(request,'login.html')
    return HttpResponseRedirect('home')
def home(request):
    global token,user_id
    # Tasks_Model(title='task2',description='task2_description', due_date='2022-01-01',status='in process').save()
    # Tasks_Model(title='task3',description='task3_description', due_date='2023-01-01',status='completed').save()
    if token=='':
        print("null token found redirecting to login")
        return HttpResponseRedirect('/')
    print("---------------------token---------------------")
    print(token)
    print("------------------------------------------------")
    print("userd id in home is",user_id)
    t=Tasks_Model.objects.all()
    tasks=[]
    for x in t:
        if x.user_id==user_id:
            tasks+=[x]
    
    return render(request,'home.html',{'tasks':tasks})
def update(request):
    global token
    print(request.POST)
    task=Tasks_Model.objects.get(pk=request.POST['id'])
    if len(str(token))==0:
        return render(request,'login.html')
    print("---------------------token---------------------")
    print(token)
    print("------------------------------------------------")
    try:
        l=request.POST['delete']
        print("in if condition to delete")
        task.delete()
        return HttpResponseRedirect('home')
    except:
        task.title=request.POST['title']
        task.description=request.POST['description']
        task.status=request.POST['status']
        task.due_date=request.POST['due_date']
        task.save()
        return HttpResponseRedirect('home')
    print(request.POST)
    print("----------------")
  
def create(request):
    global token,user_id
    if len(str(token))==0:
        return HttpResponseRedirect('/')
    title=request.POST['title']
    description=request.POST['description']
    status=request.POST['status']
    user_id=user_id
    date=request.POST['due_date']
    print("---------------------token---------------------")
    print(token)
    print("------------------------------------------------")
    Tasks_Model(title=title,user_id=user_id,description=description,status=status,due_date=date).save()
    return HttpResponseRedirect('home')
def register(request):
    global rc
    return render(request,'register.html',{'x':rc})
def register_validate(request):
    global rc
    users=Users_Model.objects.all()
    username=request.POST['username']
    for user in users:
        if user.username==username:
            rc=True
            return HttpResponseRedirect('register')
    rc=False
    Users_Model(username=username,password=request.POST['password']).save()
    return HttpResponseRedirect('/')