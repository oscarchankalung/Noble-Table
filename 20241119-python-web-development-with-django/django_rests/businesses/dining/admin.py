from django.contrib import admin
from .models import Restaurant, Review

class ReivewInline(admin.TabularInline):
    model = Review

class RestaurantAdmin(admin.ModelAdmin):
    inlines = [
        ReivewInline
    ]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Review)
