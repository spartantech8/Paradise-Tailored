from django.shortcuts import render, redirect
from .models import Question, Destination

def index(request):
    return render(request,"paradise_tailored_app/index.html")

def tailor(request):
    questions = Question.objects.all()
    context ={
        "questions":questions
    }
    return render(request,"paradise_tailored_app/tailor.html", context)

def process_survey(request):
    must_haves = []
    for k, v in request.POST.items():
        if v == "5":
            must_haves.append(k)
    must_haves={'swimming','surfing'}
    results = {}
    for m in must_haves:
        filter = m + '__gte'
        filter_kwargs = {
            filter:4
            }
        results[m] = Destination.objects.filter(**filter_kwargs)
        


    #filters = {}
    # filters[request.POST['category']]
    #category = Destination.objects.filter()
    return redirect("/matches")

def matches(request):
    return render(request,"paradise_tailored_app/matches.html")

def sample_booking(request):
    return render(request,"paradise_tailored_app/sample.html")
