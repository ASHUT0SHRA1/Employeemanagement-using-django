from django.shortcuts import redirect, render
from django.http import HttpResponse
from emp.models import *
from .forms import FeedbackForm,Formfeedback 
# Create your views here.
def emphome(request):
    emps = Emp.objects.all()
    # return HttpResponse('<p>student home page</p>')
    return render( request , "emp/home.html" , {
        'emps' : emps
    })

def addemp(request):
    if request.method == "POST":
        ename = request.POST.get("empname")
        emp_id = request.POST.get("empId")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        working = request.POST.get("working")
        department = request.POST.get("department")
        # print(name)
        e = Emp()
        e.name = ename
        e.emp_id = emp_id
        e.phone = phone 
        e.address = address  
        if working is None :
            e.working=False
        else :
            e.working=True
        e.department = department
        e.save()
        print("Data is coming")
        return redirect("/emp/emphome/")
    return render( request , 'emp/addemp.html')

def delemp(request, emp_id):
    emp=Emp.objects.get(emp_id=emp_id)
    emp.delete()
    return redirect('/emp/emphome/')


def updateEmp(request , emp_id):
    emp=Emp.objects.get(emp_id=emp_id)
    return render(request  , "emp/updemp.html" ,{'emp':emp})

def toupdateemp(request , id):
    if request.method == "POST":
        ename = request.POST.get("empname")
        emp_id_temp = request.POST.get("empId")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        working = request.POST.get("working")
        department = request.POST.get("department")
        # print(name)
        e=Emp.objects.get(pk=id)
        e.name = ename
        e.emp_id = emp_id_temp
        e.phone = phone 
        e.address = address  
        if working is None :
            e.working=False
        else :
            e.working=True
        e.department = department
        e.save()
        print("Data is coming")
        return redirect("/emp/emphome/")
    

def testimonials(request ):
    testimonials= Testimonial.objects.all()
    return render(request , "emp/testimonials.html" , {'testimonials':testimonials})

def feedback(request):
    form = Formfeedback()
    if request.method == "POST":
        form = Formfeedback(request.POST)  # Pass POST data to the form
        if form.is_valid():  # Check if the form is valid (including rating)
            form.save()
            return redirect("/emp/testimonials/")  # Redirect to success page
        else:
            # Handle the case where the form is invalid (e.g., display error messages)
            return render(request, "emp/feedback.html", {'form': form})
    return render(request, "emp/feedback.html", {'form': form})
    # if request.method == "POST":
    #     form=FeedbackForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data['email'])
    #         print(form.cleaned_data['name'])
    #         print(form.cleaned_data['feedback'])

    #         # form.save()
    #         print("data saved")
    #     else:
    #         return render(request , "emp/feedback.html" , {
    #         'form' : form
    #     })
    # else:
    #     form = FeedbackForm()
    #     return render(request , "emp/feedback.html" , {
    #         'form' : form
    #     })
        