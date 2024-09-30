from django.contrib import admin
from app1.models import user
class UserAdmin(admin.ModelAdmin):
    list_display=('user_name','email','password1','password2')
admin.site.register(user,UserAdmin)

# Register your models here.
