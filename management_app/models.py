from django.db import models

# Create your models here.



class Menu(models.Model):

    name = models.CharField(max_length=200,default="category ")

    unit = models.CharField(max_length=200,choices=[('lb', 'pound'), ('gm', 'grams'),
                                        ('kg', 'kilogram'), ('pcs', 'piece')], default='kg')
    
    description = models.CharField(max_length=400, null = True)

    def __str__(self):
        return self.name


class  Ingredients(models.Model):

    name = models.CharField(max_length=200)

    quantity_unit = models.CharField(max_length=200, choices=[("g", "gram"), ("ltr", "liter"), ("kg", "kilogram"), ("pc", "pieces"),

                                     ("tbsp", "table spoon"), ("tsp", "tea spoon")], default='kg')
    
    unit_cost_prices = models.FloatField(verbose_name="Cost Price per unit", default=0)


    def __str__(self):

        return self.name+" | Rs."+str(self.unit_cost_prices)+"/"+str(self. quantity_unit)



    

class Dishes(models.Model):

    name = models.CharField(max_length=200, default="enter dish name")

    category  = models.ForeignKey(Menu, default="Category of this product item", on_delete=models.CASCADE)

    profit = models.FloatField(default = 0, help_text = "this is calculated in percentage ")

    cost_price = models.FloatField(help_text="this is calculated using ingredint cost with its quantity", default=0)
    descriptions = models.CharField(max_length=300, null=True, blank=True)

    selling_price = models.FloatField(help_text="calculated on basis of profit", default=0)

    

    def __str__(self):
        return self.name + "  " +str(self.selling_price)+ "Rs" + "/"+ str(self.category.unit)


   
    def save(self, *args, **kwargs):
        self.cost_price = 0
        all_ingredients = Dish_ingredients.objects.filter(dish=self)
        

        for i in all_ingredients:
            ingredient_unit_cost = i.ingredient.unit_cost_prices
            
            ingredient_quantity = i.quantity
            print(ingredient_quantity, type(ingredient_quantity), "this ingredient_quantity")

            total_cost_0f_ingredient =  ingredient_unit_cost*ingredient_quantity
            self.cost_price+=total_cost_0f_ingredient

        
        self.selling_price = round(self.cost_price+(self.cost_price*(self.profit/100.0)))

        self.cost_price = round(self.cost_price)

        super(Dishes, self).save( *args, **kwargs)

    





class Dish_ingredients(models.Model):

    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)

    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)

    quantity = models.FloatField(help_text="quanity of ingredient in Dish ")


    def __str__(self):
        return self.dish.name + "|" + self.ingredient.name
    




    




	

	










