from django.db import models

# Create your models here.

class WaterUser(models.Model):
	
	username = models.CharField(max_length = 100, verbose_name = 'username')

	userphone = models.CharField(max_length = 20, verbose_name = 'userphone',default = '')

	addrress = models.CharField(max_length = 150, verbose_name = 'addrress')

	def __str__(self):
		return self.username
		

class Order(models.Model):
	"""docstring for waterModel"""
	orderid = models.AutoField(primary_key=True)

	user = models.ForeignKey(WaterUser,on_delete=models.CASCADE)

	money = models.CharField(max_length = 100)

	time = models.DateTimeField(auto_now_add = True)

	address = models.CharField(max_length = 200, verbose_name = 'orderaddress', null = True)

	orderphone = models.CharField(max_length = 20, verbose_name = 'orderphone', null = True)



class Product(models.Model):

	productid = models.AutoField(primary_key = True)
	
	name = models.CharField(max_length = 100)

	price = models.IntegerField()

	imageUrl = models.CharField(max_length = 150, null = True)

	def __str__(self):
		return self.name

	

class Order_Product(models.Model):

	order = models.ForeignKey(Order, on_delete=models.CASCADE)

	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	amount =  models.IntegerField()

















	

								