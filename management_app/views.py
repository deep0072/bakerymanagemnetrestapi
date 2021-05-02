from django.shortcuts import render
from .models import *
from . serializers import  *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .custom import IsAdminOrReadOnly

from rest_framework.generics import CreateAPIView

from django.contrib.auth import get_user_model

User = get_user_model()





# def dish(request):

#     dish = Menu.objects.get(id=1)

#     recipe = dish.dishes_set.all()




#     print(dish, "this is recipe")

#     recipe  = recipe.get().ingredients.all()

    

    # for ingredient in ingredients:
    


# @api_view(['GET', 'PUT'])
# def Recipe_view(request, pk):
#     try:
#         snippet = Dishes.objects.get(pk=1)
#         print(snippet)
#         # recipe = snippet.dishes_set.all() 
#         # ingredients = recipe.get().ingredients.all()
#         # print(ingredients)
#     except Dishes.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer1 = DishesSerializer(snippet)

#         return Response(serializer1.data)

#     if request.method == 'PUT':

#         serializer = DishesSerializer(snippet,data=request.data)
#         if serializer.is_valid():

#             serializer.save()

#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# @api_view(['GET','PUT'])
# def Ingredients_view(request):

#     try:

#         ingredients = Ingredients.objects.all()

#     except Ingredients.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


#     if request.method == 'GET':
#         serializer1 = IngredientsSerializer(ingredients, many=True)

#         return Response(serializer1.data)


#     if request.method == 'PUT':

#         serializer1 = IngredientsSerializer(ingredients, data = request.data)
#         if serializer1.is_valid():

#             serializer1.save()

#             return Response(serializer1.data)

#         return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)



    

    
    






# @api_view(['GET','PUT'])
# def Menu_list(request):
#     try:
#         menu = Menu.objects.first()
#     except Menu.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer1 = MenuSerializer(menu, many=True)

#         return Response(serializer1.data)


#     if request.method == 'PUT':

#         serializer1 = MenuSerializer(menu, data = request.data)
#         if serializer1.is_valid():

#             serializer1.save()

#             return Response(serializer1.data)

#         return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterCreateApiView(CreateAPIView):
    
    
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    

class DishesViewset(viewsets.ModelViewSet):
    queryset = Dishes.objects.all()
    
    serializer_class = DishesSerializer
    print(serializer_class, "this is for serializer admin")
    permission_classes = [IsAdminUser]


class OnlyMYDishesViewset(viewsets.ReadOnlyModelViewSet):

    queryset = Dishes.objects.all()
 
    
    serializer_class = OnlyDishesSerializer
    

    
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]

    def get_object(self):
        return self.filter_queryset(self.get_queryset)


    



class IngredientsViewset(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [IsAdminUser]


class Dish_IngredientViewset(viewsets.ModelViewSet):
    queryset = Dish_ingredients.objects.all()
    serializer_class = DishIngredientSerializer
    permission_classes = [IsAdminUser]







    