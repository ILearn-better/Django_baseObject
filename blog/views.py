from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from blog.models import Blog


"""
def blog_list(request):
    blogs = Blog.objects.all()
    context = {
        'blog_list': [
            {
                'id':blog.id,
                'title':blog.title,
            } for blog in blogs
        ]

    }
    return JsonResponse(context)
"""
def blog_list(request):
    page = request.GET.get('page',1)
    page_size =request.GET.get('page_size',20)

    blog_qs = Blog.objects.all()
    paginator = Paginator(blog_qs,page_size)

    current_page = paginator.get_page(page)
    blogs =current_page.object_list

    context = {
        'blog_list':[
            {
                'id':blog.id,
                'title':blog.title,
            } for blog in blogs
        ],
        'paginator':{
            'total_count':paginator.count,
            'num_pages':paginator.num_pages,
            'page_size':paginator.per_page,
            'page_number':current_page.number,
        }
    }
    return JsonResponse(context)

def blog_detail(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {
        'blog':{
            'id':blog.id,
            'title':blog.title,
            'content':blog.content,
            'author':{
                'id':blog.author.id,
                'username':blog.author.username,
                    }
        }
    }

    return JsonResponse(context)
# Create your views here.
