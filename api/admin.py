from django.contrib import admin
from .models import User, Craftsman, Apprentice, Category, Order, Job


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_craftsman", "is_apprentice")
    list_filter = ("is_craftsman", "is_apprentice")
    search_fields = ("username", "email")


@admin.register(Craftsman)
class CraftsmanAdmin(admin.ModelAdmin):
    list_display = ("user", "surname", "telephone", "address", "skills")
    search_fields = ("user__username", "surname", "telephone")
    list_filter = ("skills",)


@admin.register(Apprentice)
class ApprenticeAdmin(admin.ModelAdmin):
    list_display = ("user", "skill_to_learn", "category")
    search_fields = ("user__username", "skill_to_learn", "category__name")
    list_filter = ("category",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "description", "status")
    search_fields = ("user__username", "category__name", "status")
    list_filter = ("status", "category")


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("craftsman", "order", "status")
    search_fields = ("craftsman__user__username", "order__description", "status")
    list_filter = ("status",)