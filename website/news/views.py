from django.shortcuts import render

# Create your views here.

def Helloworld(request):
    context={
       'person':['Ali jama',30,'Computer science','New Generation']
    }
    return render(request, 'blog/index.html',context)
