from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def balls_in_box(request):
    return render(request, 'balls_in_box.html')

def monty_hall(request):
    return render(request, 'monty_hall.html')

def rare_disease(request):
    return render(request, 'rare_disease.html')