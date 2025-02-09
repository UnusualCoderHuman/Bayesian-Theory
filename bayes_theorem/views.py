from django.shortcuts import render
from .forms import BoxInputForm, BoxCForm

from .config import correct_answers_for_box

# Create your views here.
def home(request):
    return render(request,'home.html')



def balls_in_box(request):
    message = ""
    selected_box = ""  # To know which box content to show on error (if needed)
    form = BoxInputForm()  # Create a new form instance
    # form2 = BoxCForm()
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


def box_c_view(request):
    message = ""
    red_balls = None
    blue_balls = None
    probability_answer = None

    if request.method == "POST":
        form = BoxCForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Step 1: Handle red/blue balls input
            if form.cleaned_data['red_balls'] is not None and form.cleaned_data['blue_balls'] is not None:
                red_balls = form.cleaned_data['red_balls']
                blue_balls = form.cleaned_data['blue_balls']
                # Calculate probability based on the balls entered
                total_balls = red_balls + blue_balls
                correct_probability = red_balls / total_balls if total_balls > 0 else 0
                
                # Step 2: Handle the probability question
                if form.cleaned_data['probability_answer'] is not None:
                    probability_answer = form.cleaned_data['probability_answer']
                    
                    # Check if the probability answer is correct
                    if probability_answer == correct_probability:
                        message = f"✅ Correct! The probability of selecting a red ball is {correct_probability:.2f}."
                    else:
                        message = f"❌ Incorrect. The correct probability is {correct_probability:.2f}."
            else:
                message = "⚠️ Please enter valid numbers for red and blue balls."
        else:
            message = "⚠️ Please enter valid values."

    else:
        form = BoxCForm()

    return render(request, "balls_in_box.html", {
        'form': form,
        'message': message,
        'red_balls': red_balls,
        'blue_balls': blue_balls,
        'probability_answer': probability_answer
    })

def monty_hall(request):
    return render(request, 'monty_hall.html')

def rare_disease(request):
    return render(request, 'rare_disease.html')



