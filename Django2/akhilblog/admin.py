#admin.py
'''
from django.contrib import admin
from akhilblog.models import Cert, UserProfile 
admin.site.register(Cert)
admin.site.register(UserProfile) 
'''
from django.contrib import admin
from akhilblog.models import Post

admin.site.register(Post)
