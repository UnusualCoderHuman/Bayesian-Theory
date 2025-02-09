from django.shortcuts import render
from .forms import BoxInputForm, BoxCForm

from .config import correct_answers_for_box
probablity_holder = 0
# Create your views here.
def home(request):
    return render(request,'home.html')



def balls_in_box(request):
    message = ""
    selected_box = ""  # Track selected box
    form = BoxInputForm(request.POST or None)  # Form for Box A and B
    form_c = BoxCForm(request.POST or None)  # Form for Box C

    # Default values for Box C
    red_balls = request.session.get("red_balls", None)
    blue_balls = request.session.get("blue_balls", None)
    probability_answer = request.session.get("probability_answer", "")

    if request.method == "POST":
        box = request.POST.get("box")  # Identify which box is being processed
        selected_box = box  # Ensure the correct box remains visible after submission

        print("POST data:", request.POST)  # Debugging to check what is sent in POST

        if box in ["A", "B"]:  # Handling predefined boxes
            if form.is_valid():
                user_value = form.cleaned_data["user_input"]
                correct_answer = correct_answers_for_box[box]
                message = "✅ That's correct!" if user_value == correct_answer else "❌ That's wrong. Try again."
        
        elif box == "C":  # Handling customizable Box C
            if form_c.is_valid():
                # Step 1: Handle red and blue balls input
                red_balls = form_c.cleaned_data.get("red_balls")
                blue_balls = form_c.cleaned_data.get("blue_balls")

                # Store in session to persist across refreshes
                request.session["red_balls"] = red_balls
                request.session["blue_balls"] = blue_balls

                # Step 2: Calculate the correct probability
                if red_balls is not None and blue_balls is not None:
                    total_balls = red_balls + blue_balls
                    correct_probability = red_balls / total_balls if total_balls > 0 else 0
                    request.session["correct_probability"] = correct_probability
                    message = f"Red Balls: {red_balls}, Blue Balls: {blue_balls}. Now, enter the probability of selecting a red ball."

                # Step 3: Handle probability input
                probability_answer = form_c.cleaned_data.get("probability_answer")
                print("Probability Answer from form_c:", probability_answer)  # Check what the form is giving
                request.session['probability_answer'] = probability_answer

                # Step 4: Check the probability answer
                if probability_answer is not None:
                    correct_probability = request.session.get("correct_probability", 0)
                    
                    if probability_answer == correct_probability:
                        message = f"✅ Correct! The probability of selecting a red ball is {correct_probability:.2f}."
                    else:
                        message = f"❌ Incorrect. The correct probability is {correct_probability:.2f}."
                else:
                    message = "⚠️ Please enter a probability answer."

            else:
                message = "⚠️ The form data was invalid. Please try again."

    context = {
        "form": form,
        "form_c": form_c,
        "message": message,
        "selected_box": selected_box,
        "red_balls": red_balls,
        "blue_balls": blue_balls,
        "probability_answer": probability_answer,
    }
    return render(request, "balls_in_box.html", context)




# def balls_in_box(request):
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




# def box_c_view(request):
    message = ""
    red_balls = None
    blue_balls = None
    probability_answer = None

    if request.method == "POST":
        form = BoxCForm(request.POST)

        # Step 1: Handling the red and blue balls input
        if 'red_balls' in request.POST and 'blue_balls' in request.POST:
            if form.is_valid():
                red_balls = form.cleaned_data['red_balls']
                blue_balls = form.cleaned_data['blue_balls']

                # Calculate the probability
                total_balls = red_balls + blue_balls
                correct_probability = red_balls / total_balls if total_balls > 0 else 0
                message = f"Red Balls: {red_balls}, Blue Balls: {blue_balls}. Now, enter the probability of red."

                return render(request, "balls_in_box.html", {
                    'form': form,
                    'message': message,
                    'red_balls': red_balls,
                    'blue_balls': blue_balls,
                    'probability_answer': probability_answer,
                    'selected_box': 'C'  # Ensure Box C remains visible
                })

        # Step 2: Handling the probability input
        elif 'probability_answer' in request.POST:
            if form.is_valid():
                probability_answer = form.cleaned_data.get('probability_answer', None)

                # Get red and blue balls from the request (since we removed session usage)
                red_balls = int(request.POST.get('red_balls', 0))
                blue_balls = int(request.POST.get('blue_balls', 0))

                # Calculate the correct probability
                total_balls = red_balls + blue_balls if red_balls and blue_balls else 0
                correct_probability = red_balls / total_balls if total_balls > 0 else 0

                if probability_answer is not None:
                    if float(probability_answer) == correct_probability:
                        message = f"✅ Correct! The probability of selecting a red ball is {correct_probability:.2f}."
                    else:
                        message = f"❌ Incorrect. The correct probability is {correct_probability:.2f}."
                else:
                    message = "⚠️ Please enter a valid probability."
            else:
                message = "⚠️ The form data was invalid. Please try again."
    else:
        form = BoxCForm()

    return render(request, "balls_in_box.html", {
        'form': form,
        'message': message,
        'red_balls': red_balls,
        'blue_balls': blue_balls,
        'probability_answer': probability_answer,
        'selected_box': 'C'  # Ensure Box C remains visible
    })

# def box_c_view(request):
    message = ""
    red_balls = None
    blue_balls = None
    probability_answer = None

    if request.method == "POST":
        form = BoxCForm(request.POST)

        # Step 1: Handling the red and blue balls input
        if 'red_balls' in request.POST and 'blue_balls' in request.POST:
            if form.is_valid():
                red_balls = form.cleaned_data['red_balls']
                blue_balls = form.cleaned_data['blue_balls']
                # Store the red and blue balls for later use

                # Calculate the probability
                total_balls = red_balls + blue_balls
                correct_probability = red_balls / total_balls if total_balls > 0 else 0
                message = f"Red Balls: {red_balls}, Blue Balls: {blue_balls}. Now, enter the probability of red."

                # Store the red and blue ball values in the session or in context
                request.session['red_balls'] = red_balls
                request.session['blue_balls'] = blue_balls
                return render(request, "balls_in_box.html", {
                    'form': form,
                    'message': message,
                    'red_balls': red_balls,
                    'blue_balls': blue_balls,
                    'probability_answer': probability_answer
                })

        # Step 2: Handling the probability input
        elif 'probability_answer' in request.POST:
            # Get the red and blue balls from session data
            red_balls = request.session.get('red_balls', 0)
            blue_balls = request.session.get('blue_balls', 0)

            # Check if the form is valid before accessing cleaned_data
            if form.is_valid():
                # Access cleaned data for probability_answer
                probability_answer = form.cleaned_data.get('probability_answer', None)

                # Calculate the correct probability
                total_balls = red_balls + blue_balls if red_balls is not None and blue_balls is not None else 0
                correct_probability = red_balls / total_balls if total_balls > 0 else 0

                # Check the user's probability answer
                if probability_answer is not None:
                    if probability_answer == correct_probability:
                        message = f"✅ Correct! The probability of selecting a red ball is {correct_probability:.2f}."
                    else:
                        message = f"❌ Incorrect. The correct probability is {correct_probability:.2f}."
                else:
                    message = "⚠️ Please enter a valid probability."
            else:
                message = "⚠️ The form data was invalid. Please try again."
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



