from django.contrib import admin
from .models import User, Product, Comment, Ranking, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Ranking)
admin.site.register(Category)