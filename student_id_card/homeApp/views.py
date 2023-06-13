from django.shortcuts import render
from django.http import HttpResponse


import qrcode
 
def qr_generator(data,roll):
    
    qr = qrcode.QRCode(version = 1,
                    box_size = 10,
                    border = 5)
    qr.add_data(data)
    
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black',
                        back_color = 'white')
    
    img.save(f'{roll}.png')

# qr_generator("Rafe",121)



# Create your views here.
def home(request):
    print(request)
    if request.method == "POST":
        # pass
        full_name = request.POST.get('fullname')
        roll = request.POST.get('roll')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        department = request.POST.get('department')
        shift = request.POST.get('shift')
        blood = request.POST.get('blood')
        section = request.POST.get('section')
        adress = request.POST.get('adress')
        
        
        data = f'{full_name}\n{roll}\n{father}\n{mother}\{department}\n{shift}\n{blood}\n{section}\n{adress}\n'
        qr_generator(data,roll)
    
    return render(request,'home.html')
