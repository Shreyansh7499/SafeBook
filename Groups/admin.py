from django.contrib import admin
from .models import Group,Group_post,Group_join_request

admin.site.register(Group)
admin.site.register(Group_post)
admin.site.register(Group_join_request)