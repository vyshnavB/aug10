from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Follower)
admin.site.register(intrest)
admin.site.register(page)
admin.site.register(level2)
admin.site.register(friend_request)
admin.site.register(Notifications)