from django.db.models import Count
from blogapp.models import Post
from django.db import connection

def getRightInfo(request):
    #查询分类信息
    r_postList = Post.objects.values('category','category__cname').annotate(c=Count('*')).order_by('-c')

    #查询归档信息
    cursor = connection.cursor()
    cursor.execute("select created,count('*') as c from blogapp_post group by DATE_FORMAT(created,'%Y-%m') order by c desc")
    createdPost = cursor.fetchall()
    #查询近期文章
    recentPost = Post.objects.order_by('-id')[:3]
    return {'r_postList':r_postList,'createdPost':createdPost,'recentPost':recentPost}

