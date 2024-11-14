from django.contrib import admin

from users.models import CustomUser
#
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'email']
#     list_filter = ['user', 'stars_given']
#     search_fields = ['user']


admin.site.register(CustomUser)
