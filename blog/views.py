from django.shortcuts import render, redirect
from .models import Blog, Category
from django.contrib.auth import authenticate, login
from .forms import BlogForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm


#   CRUD - Create, Retrieve, Update, Delete

def blog_list(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories,
    }
    return render(request, 'blog/blog_list.html', context)



def blog_detail(request, pk, slug):
    blog = Blog.objects.get(id=pk, slug=slug)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog_detail.html', context)


def category_filter(request, pk):

    blogs = Blog.objects.filter(category=pk)
    categories = Category.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories,
    }
    return render(request, 'blog/category.html', context)



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def user_login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog_list') 
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})               


def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/create.html', context)

def update(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(request.POST or None, request.FILES, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    context = {
        'form': form,
    }
    return render(request, 'blog/update.html', context)

def delete(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    context = {
        'blog': blog,
    }
    return render(request, 'blog/delete.html', context)


