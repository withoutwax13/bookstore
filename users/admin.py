from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomChangeForm, CustomCreationForm

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):

    add_form = CustomCreationForm
    form = CustomChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)