from django.contrib import admin
from blogapp.models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)