from django.contrib import admin

# Register your models here.
from .models import Role , User,Permissions


admin.site.register(Role)
admin.site.register(User)
admin.site.register(Permissions)