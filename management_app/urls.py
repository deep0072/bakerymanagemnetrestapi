from django.urls import path ,include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()


router.register('ingredient', views.IngredientsViewset),
router.register('Menu', views.DishesViewset, 'menu'),
router.register('Dishes/', views.OnlyMYDishesViewset, 'mydish'),

router.register('Dish_ingredients', views.Dish_IngredientViewset)






urlpatterns = [
   
   path('', include(router.urls)),
   path('account_register',views.RegisterCreateApiView.as_view(), name='register')

]	 
    
