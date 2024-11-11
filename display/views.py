from django.shortcuts import render
from Poll.models import QuizQuestions

# Create your views here.
def display(request):
    questions = QuizQuestions.objects.all()
    context = {'questions': questions}
    return render(request, 'output.html', context)