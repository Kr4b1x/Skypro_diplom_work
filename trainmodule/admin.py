from django.contrib import admin
from .models import TrainModel
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin for User model
    """
    list_display = ("email",)
    search_fields = ("email",)


admin.site.register(TrainModel)
