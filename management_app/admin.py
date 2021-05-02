from django.contrib import admin

from .models import *

admin.site.register(Menu)
admin.site.register(Ingredients)
admin.site.register(Dishes)
admin.site.register(Dish_ingredients)


# Register your models here.
