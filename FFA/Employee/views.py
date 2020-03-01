from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def save_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                pass
    else:
        form = EmployeeForm()
    return render(request,"index.html",{"form":form})

def show(request):
    employee = Employee.object.all()
    return render(request,"show.html")

