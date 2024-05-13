from django.contrib import admin
from .models import Product, Image


class ImageInline(admin.TabularInline):  # Используем TabularInline для удобного отображения изображений
    model = Image
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    inlines = [ImageInline]  # Добавляем встроенный класс изображений к админке продуктов
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Image)  # Регистрируем модель Image в админке
