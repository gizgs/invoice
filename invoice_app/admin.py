from django.contrib import admin
from django.contrib.auth.models import User
from .models import Invoice


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Invoice)
# Register your models here.
