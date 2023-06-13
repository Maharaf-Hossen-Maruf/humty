from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print(request)
    if request.method == "POST":
        # pass
        full_name = request.POST.get('fullname')
        roll = request.POST.get('roll')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        deratment = request.POST.get('deratment')
        shift = request.POST.get('shift')
        blood = request.POST.get('blood')
        section = request.POST.get('section')
        adress = request.POST.get('adress')
        
        
        print(full_name,roll,section,adress,father,mother,deratment,blood,shift)
    
    return render(request,'home.html')
