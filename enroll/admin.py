from django.contrib import admin
from .models import User,Register

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','contact')


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','username','email','password1','password2')
    