import math
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def indexview(request,num=1):
    num = int(num)
    #查询所有帖子信息
    postlist = Post.objects.all().order_by('-created')
    #分页
    pageobj = Paginator(postlist,1)
    #获取当前页的数据
    pagelist = pageobj.page(num)
    #获取当前页面中的所有页码数(页码列表)
    start = num - int(math.ceil(10.0/2))
    if start < 1:
        start = 1
    end = start + 9
    if end > pageobj.num_pages:
        end = pageobj.num_pages
    if end < 10:
        start = 1
    else:
        start = end - 9
    paglist = range(start,end+1)
    return render(request,'index.html',{'postlist':pagelist,'pagelist':paglist,'currentnum':num})


def detailview(request,postid):
    postid = int(postid)
    #根据postid查询post详情
    postobj = Post.objects.get(id=postid)

    return render(request,'detail.html',{'post_obj':postobj})


def article_view(request,categoryid):
    categoryid = int(categoryid)
    plist = Post.objects.filter(category_id=categoryid)
    return render(request,'article.html',{'plist':plist})


def archive_view(request,y=-1,m=-1):
    y = int(y)
    m = int(m)
    #根据发帖的年份来查询数据
    if y==-1 and m==-1:
        plist = Post.objects.all()
    else:
        plist = Post.objects.filter(created__year=y,created__month=m)
    return render(request, 'article.html', {'plist': plist})