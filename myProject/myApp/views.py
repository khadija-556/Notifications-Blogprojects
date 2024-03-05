from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from myApp.forms import *
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def singinPage(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
           
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            
            user=authenticate(username =username,password = password)
            login(request,user)
            return redirect("homePage")
    else:
            form=LoginForm()

    
    
    return render(request,'singin.html',{'form':form})

def singupPage(request):
    if request.method == 'POST':
        form=customUserForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("singinPage")
    else:
        form=customUserForm()
        
    
    return render(request,'singup.html',{'form':form})
def homePage(request):
    return render(request, "home.html")

def logoutPage(request):
    logout(request)
    return redirect("singinPage")


def blogPage(request):
    if request.method == "POST":
        form=blogForm(request.POST,request.FILES)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.user=request.user
            form2.save()
            return redirect("blogPage")
    else:
        form=blogForm()
    
    return render(request, "blogPage.html",{'form':form})

def viewblog(request):
    task=BlogModel.objects.all()
  
    return render(request,"viewblog.html",{'task':task})


def viewblogDeletePage(request, id):
    BlogModel.objects.filter(id=id).delete()
    
    messages.success(request, 'viewblog Delete Successfully!')

    return redirect('viewblog')

def editBlog(request, id):
    obj=BlogModel.objects.get(id=id)
    if request.method == 'POST':
        form = BlogModel(request.POST, instance=obj) 
        if form.is_valid():
            form.save()
            return redirect("viewblog")

    else:
        form = BlogModel(instance=obj) 


    return render(request, 'editBlog.html', {'form': form})

def search_results(request):
    query = request.GET.get('query')
    
    recipes = BlogModel.objects.filter(
        Q(blog_title__icontains=query) 
       
    ).distinct()

    return render(request, 'search_results.html', {'recipes': recipes, 'query': query})

def profilePage(request):
    profile=writterModelForm()
    return render(request,"profile.html", {'profile': profile})