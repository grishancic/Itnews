from django.shortcuts import render
from .forms import TableForm

def appl(request):
   if request.method=='POST':
     form=TableForm(request.POST)
     form.save()
   form = TableForm()
   context={'form':form}

   return render(request, "main/index.html",context)


def home(request):
    return render(request, 'main/home.html')
def cont(request):
    return render(request, 'main/contact.html')
def port(request):
    return render(request, 'main/portfolio.html')