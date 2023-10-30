from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import UserProfile, Address, Device, Simcard, Task, UserVehicle, Vehicle


class CustomAdmin(UserAdmin):
    readonly_fields = ("last_login", "date_joined", "date_blocked", "date_updated")
    fieldsets = (
        (
            "Credentials",
            {
                "fields": (
                    "username",
                    "password",
                ),
            },
        ),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "ssn",
                    "birthday",
                    "address",
                    "asaas_token",
                    "phone1",
                    "phone2",
                    "bio",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_tech",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                    "date_blocked",
                    "date_updated",
                ),
            },
        ),
    )


admin.site.register(UserProfile, CustomAdmin)
admin.site.register(Address)
admin.site.register(Device)
admin.site.register(Simcard)
admin.site.register(Task)
admin.site.register(UserVehicle)
admin.site.register(Vehicle)
