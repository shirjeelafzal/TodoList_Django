from django.shortcuts import render,HttpResponse
# Create your views here.
def todo_add(request):
    if request.method=='GET':
        return render(request,"add_get.html")