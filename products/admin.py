from django.contrib import admin
from .models import CategoryProducts, Review, Clothes

# Register your models here.

admin.site.register(CategoryProducts)
admin.site.register(Review)
admin.site.register(Clothes)
