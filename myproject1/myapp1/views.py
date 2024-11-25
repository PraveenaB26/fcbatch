from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
#views.py
from .models import Person

#from .models import Person
#from .models import Post
#from rest_framework.decorators import api_view, permission_classes
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.response import Response
#from rest_framework import viewsets
#from .models import Item
#from .serializers import ItemSerializer
#from .forms import Userinfoform


'''

# Create your views here.
def wel(request):
    return HttpResponse("welcome home")
def hello(request):
    return HttpResponse("hello all")
def fun4(request):
    a=100
    return HttpResponse(a)
def fun5(request):
    new=fun4(request)
    return HttpResponse(new)
'''

def add_db(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        Person.objects.create(name=name,age=age)
        return HttpResponse ("data added successfully")
        #return HttpResponseRedirect('/success')
    return render(request, 'add_db.html')
'''
def success(request):
    persons = Person.objects.all()
    print(persons)
    return render(request, "success.html",{"persons":persons})
def delete(request,pername,perage):
    pers=Person.objects.get(name=pername)
    pers.delete()
    return HttpResponseRedirect("/success")
def update(request,pername,perage):
    person=Person.objects.get(name=pername)
    if request.method=="POST":
        newname=request.POST.get("name")
        newage=request.POST.get("age")
        person.name=newname
        person.age=newage
        person.save()
        return redirect("/success")
    return render(request,"update.html",{"person":person})

def post_list(request):
    posts=Post.objects.all()
    return render(request, 'post_list.html',{'posts':posts})
def post_detail(request, pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request, 'post_detail.html',{'post':post})


def index(request):
    if 'name' in request.session:
        name = request.session['name']
        return HttpResponse(f"Hello, {name}! Welcome back.")
    return render(request, 'session.html')
def set_name(request):
    if request.method =="POST":
        name = request.POST.get('name')
        request.session['name'] = name
        return HttpResponse("Name stored in session.")
    return HttpResponse("Invalid request.")
def delete_name(request):
    if 'name' in request.session:
        del request.session['name']
        return HttpResponse("Name deleted from session.")
    return HttpResponse("No name found in session.")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request):
    content = {'message': 'Authenticated!'}
    return Response(content)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



def user_info(request):
    if request.method =='POST':
        form = Userinfoform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(f"Name: {name}, Email: {email}")
    else:
        form = Userinfoform()
    return render(request, 'user_info.html',{'form': form})
    
'''



