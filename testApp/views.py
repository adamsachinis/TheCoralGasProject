from django.shortcuts import render, get_object_or_404
from .models import Question,GasTanks

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. From the app re arxidi! You're at the polls index.")

def index2(request):
    return HttpResponse("Hello, world. From the app re arxidi gamimeno auto einai to index 2! You're at the polls index.")


def about(request):
    gasTankList = GasTanks.objects.all()
    return render(request, "testApp/about.html",{"gasTankList":gasTankList})
  
def dynamic(request,gasTankId):
    gasTank = get_object_or_404(GasTanks, pk=gasTankId)
    return render(request,"testApp/contact.html",{"gasTank":gasTank})



def index3(request):
    latest_question_list = Question.objects.all()
    context = {"latest_question_list": latest_question_list}
    return render(request, "testApp/index.html", context)