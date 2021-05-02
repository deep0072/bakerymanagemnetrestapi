from rest_framework import serializers


from . models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):



	email1 = serializers.EmailField(label="Email")

	email2 = serializers.EmailField(label="Confirm Email")

	password2 = serializers.CharField(label="Confirm password", style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User

		fields = (

			'username',
			'email1',
			'email2',
			'password',
			'password2'


		)

		extra_kwargs = {'password':{'write_only':True }}
			

	def validate_data(self,value):
		data = self.get_initial()
		username = data['username']
		email1 = data['email1']
		email2 = value
		password1 = data['password']
		password2 = value

		user_qs_email = User.objects.filter(email=email1)
		user_qs_username = User.objects.filter(username=username)
		if user_qs_username.exists():
			raise serializers.ValidationError("this username is already exist")


		if user_qs_email.exists():
			raise serializers.ValidationError("this email is already exist")


		elif email1 != email2:
			raise serializers.ValidationError("Email must be match")

		elif password1 != password2:
			raise serializers.ValidationError("password  must be match")

		return value

	def create(self, validate_data):

		username = validate_data['username']

		email1 = validate_data['email1']

		password = validate_data['password']

		

		user_obj = User(
			username = username,
			email = email1


		)
		user_obj.set_password(password)
		user_obj.save()

		return validate_data










class IngredientsSerializer(serializers.ModelSerializer):

	class Meta:

		model = Ingredients
		
		fields = '__all__'

		




class DishesSerializer(serializers.ModelSerializer):
	

	class Meta:

		model = Dishes
		fields = '__all__'


class OnlyDishesSerializer(serializers.ModelSerializer):
	

	class Meta:

		model = Dishes

		fields = ('name', 'selling_price', 'descriptions')

		



		




class DishIngredientSerializer(serializers.ModelSerializer):
	

	class Meta:

		model = Dish_ingredients
		fields = '__all__'










	

		



		




		
		