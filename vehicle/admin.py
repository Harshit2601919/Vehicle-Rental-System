from django.contrib import admin
from .models import *


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('number_plate', 'approval_status')  # Display number plate and approval status in the admin list
    list_filter = ('approval_status',)  # Add a filter for approval status
    actions = ['approve_selected']  # Add a custom action to approve selected vehicles

    def approve_selected(self, request, queryset):
        queryset.update(approval_status='approved')  # Update the approval status of selected vehicles to 'approved'

    approve_selected.short_description = "Approve selected vehicles"

admin.site.register(Vehicle,VehicleAdmin)



# Register your models here.
