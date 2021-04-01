from django.contrib import admin

from .models import Complaint, Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner",)
    readonly_fields = ("created_at",)
    list_display = (
        "address", "price", "new_building", "construction_year", "town",
    )
    list_editable = ("new_building",)
    list_filter = ("new_building", "rooms_number", "has_balcony",)
    raw_id_fields = ("likes",)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("about_flat",)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
