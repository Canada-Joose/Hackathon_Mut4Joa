from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
admin.site.register(User, UserAdmin)

#user model에 대한 추가 필드는 따로 admin페이지에 나타나지 않기 때문에 
#custom fields라는 섹션 아래 nickname field를 추가!
# UserAdmin.fieldsets += ("Custom fields", {"fields": ("nickname",)})

UserAdmin.fieldsets +=(("Custom fields", {"fields": ("nickname",)}),)
