from django.contrib import admin

from newspaper.models import Category, Post, Tag, UserProfile, Comment, Contact


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Contact)
