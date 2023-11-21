from django.contrib import admin
from todo.models import Task ,File,History,User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "name", "is_admin","view","edit"]
    list_filter = ["is_admin","view","edit"]
    fieldsets = [
        ('User Credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name"]}),
        ("Permissions", {"fields": ["is_admin","view","edit"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "password1", "password2","view","edit"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = []
class GeneralAdmin(admin.ModelAdmin):
    list_display=['id']


admin.site.register(User, UserAdmin)
admin.site.register(History, GeneralAdmin)
admin.site.register(File, GeneralAdmin)
admin.site.register(Task, GeneralAdmin)



