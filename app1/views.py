from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')