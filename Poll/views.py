from http.client import HTTPResponse

from django.shortcuts import render , HttpResponse, redirect
from .models import QuizQuestions
from django.db import connection
from .forms import DataForm


# Create your views here.

def index (request):
    context = {
        'var1' : 'Avighn',
    }
    return render(request, "index.html", context)
   # return HttpResponse ("welcome to the polling system ...!")


from .models import QuizQuestions  # Import your models

def show_data(request):
    data = QuizQuestions.objects.all()  # Query all rows from the model
    return render(request, 'show_all_questions.html', {'data': data})

def success_view(request):
    return render(request, 'success.html')


# views.py

def add_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            # Extract data from form fields
            new_question = form.cleaned_data['new_question']
            correct_option = form.cleaned_data['correct_option']
            option1 = form.cleaned_data['option1']
            option2 = form.cleaned_data['option2']
            option3 = form.cleaned_data['option3']
            option4 = form.cleaned_data['option4']

            # Execute raw SQL to insert data into MySQL
            with connection.cursor() as cursor:
                sql_query = "INSERT INTO quiz_questions (question, option_a, option_b, option_c, option_d, correct_option) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql_query, [new_question, option1, option2, option3, option4, correct_option])

            return redirect('success')  # Redirect to a success page or another view
    else:
        form = DataForm()

    return render(request, 'add_data.html', {'form': form})


#