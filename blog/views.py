from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import New
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    return render(request, 'home.html')

def list(request):
    blogs = Blog.objects.all()

    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)   
    except PageNotAnInteger:
        posts = paginator.get_page(1)

    return render(request, 'list.html', {'blogs':blogs,'posts':posts})

def new(request):

    if request.method == 'POST':

        form = New(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
        return redirect('list')
            
    else:

        form = New()
        return render(request, 'new.html', {'form': form})

def detail(request, blog_id):

    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request,'detail.html', {'blog_detail':blog_detail})

def delete(request, blog_id):

    blog_delete = get_object_or_404(Blog, pk = blog_id)
    blog_delete.delete()
    return redirect('/')

def edit(request, blog_id):

    blog_edit = get_object_or_404(Blog, pk = blog_id)

    if request.method == 'POST':
        blog_edit.title = request.POST['title']
        blog_edit.body = request.POST['body']
        blog_edit.save()
        
        return redirect('/blog/'+str(blog_edit.id))

    else:

        return render(request, 'edit.html', {'blog_edit':blog_edit})
    