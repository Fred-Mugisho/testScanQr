from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'test_cam/index.html')

def scanning_page(request):
    if request.method =="POST":
        matricule = request.POST.get('matricule')
        messages.error(request, f"La donnée extraite du code qr {matricule}")
        return redirect('scanning_page')
    return render(request, 'test_cam/scanning_page.html')
