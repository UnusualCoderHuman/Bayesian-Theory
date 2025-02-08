from django.shortcuts import render
from .forms import BoxInputForm
from .config import correct_answers_for_box

# Create your views here.
def home(request):
    return render(request,'home.html')



def balls_in_box(request):
    message = ""
    selected_box = ""  # To know which box content to show on error (if needed)
    form = BoxInputForm()  # Create a new form instance

    if request.method == "POST":
        # print("POST request reiveved")
        form = BoxInputForm(request.POST)
        # Get the hidden box identifier
        # print("Form data:", request.POST)
        box = request.POST.get('box')
        selected_box = box  # So that we can ensure the appropriate box content is visible after submission
        
        if form.is_valid() and box in correct_answers_for_box:
            user_value = form.cleaned_data["user_input"]
            correct_answer = correct_answers_for_box[box]
            if user_value == correct_answer:
                message = "✅ That's correct!"
            else:
                message = "❌ That's wrong. Try again."
        else:
            message = "⚠️ Please enter a valid number."
            
    
    context = {
        "form": form,
        "message": message,
        "selected_box": selected_box,
    }
    return render(request, "balls_in_box.html", context)


def monty_hall(request):
    return render(request, 'monty_hall.html')

def rare_disease(request):
    return render(request, 'rare_disease.html')



