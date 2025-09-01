# In animals/admin.py
from django.contrib import admin
from .models import Animal, Donation, Volunteer, CustomUser
from django.contrib.auth.admin import UserAdmin


# Custom admin for CustomUser to handle deletion
class CustomUserAdmin(UserAdmin):
    def delete_model(self, request, obj):
        # Custom logic before deleting the user
        # For example, delete related records or perform other cleanup actions
        super().delete_model(request, obj)


# Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal_type', 'location', 'rescue_needed', 'food_supply_needed', 'added_by')
    list_filter = ('animal_type', 'rescue_needed', 'food_supply_needed')
    search_fields = ('name', 'location', 'description')


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'email', 'amount', 'date')
    list_filter = ('donor_name', 'amount')
    search_fields = ('donor_name', 'email')


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_number', 'address', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user__username', 'contact_number', 'address')

