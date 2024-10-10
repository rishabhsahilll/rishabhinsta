from django.contrib import admin
from .models import Post, Comment, PostReport,Twit, TwitComment, TwitReport

# Registers blog app the django admin backend.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostReport)
admin.site.register(Twit)
admin.site.register(TwitReport)
admin.site.register(TwitComment)

