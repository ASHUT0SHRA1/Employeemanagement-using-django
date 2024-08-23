
from django.http import HttpResponse
from django.shortcuts import render
import datetime
def test(request):
    date=datetime.datetime.now()
    if request.method=="POST":
        check=request.POST['check']
        print(check)
    print("test function is called from view ")
    return HttpResponse("<h1>Hello from view </h1>" + str(date) )
    # return render(request,"about.")

def about(request):
    # return HttpResponse("<h1>This is about About page</h1>")
    return render(request,"about.html" , {})
def home(request):
    # return HttpResponse('<h1>Home</h1>')
    date=datetime.datetime.now()
    isActive = False
    if request.method =="POST" : 
        isActive=request.POST.get("checkisActive")
    name="Learncode with durgesh"
    list_of_program = [
        'wap to check even or odd',
        'wap to check prime number', 
        'wap to print all prime number 1 to 100',
        'wap to print pascal triangle'
    ]
    student={
        'std_name':"AShutosh" ,
        'std_college':"IIM ahemdabad",
        'std_city':"Ranchi"
    }
    data ={
        'date' : date,
        'isActive' : isActive , 
        'name' : name , 
        'list_of_program' : list_of_program , 
        'student_data' : student
    }
    return render(request , "home.html" , data)