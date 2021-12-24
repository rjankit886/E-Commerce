from django.db import models

# Create your models here.
class Seller(models.Model):
	name = models.CharField(max_length = 30)
	uname = models.CharField(max_length = 50)
	email = models.EmailField()
	phone = models.CharField(max_length = 20, default = None, blank = True)
	bankName = models.CharField(max_length = 50, default = None, blank = True)
	ifscCode = models.CharField(max_length = 20, default = None, blank = True)
	accountNumber = models.CharField(max_length = 20, default = None, blank = True)
	total = models.IntegerField(default = None, blank = True, null = True)

	def __str__(self):
		return str(self.id)+' '+self.name

class Category(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return str(self.id)+' '+self.name

class Brand(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return str(self.id)+' '+self.name

class Product(models.Model):
	stock = models.BooleanField(default = False)
	name = models.CharField(max_length = 50)
	desc = models.TextField()
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
	seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
	basePeice = models.FloatField()
	discount = models.FloatField(default = 0, null = True, blank = True)
	finalPrice = models.FloatField(default = 0, null = True, blank = True)
	red = models.BooleanField(default = False, blank = True, null = True)
	green = models.BooleanField(default = False, blank = True, null = True)
	black = models.BooleanField(default = False, blank = True, null = True)
	white = models.BooleanField(default = False, blank = True, null = True)
	pink = models.BooleanField(default = False, blank = True, null = True)
	xs = models.BooleanField(default = False, blank = True, null = True)
	s = models.BooleanField(default = False, blank = True, null = True)
	m = models.BooleanField(default = False, blank = True, null = True)
	l = models.BooleanField(default = False, blank = True, null = True)
	xl = models.BooleanField(default = False, blank = True, null = True)
	xxl = models.BooleanField(default = False, blank = True, null = True)
	img1 = models.ImageField(upload_to = 'images/', default = None, blank = True)
	img2 = models.ImageField(upload_to = 'images/', default = None, blank = True)
	img3 = models.ImageField(upload_to = 'images/', default = None, blank = True)
	img4 = models.ImageField(upload_to = 'images/', default = None, blank = True)
	img5 = models.ImageField(upload_to = 'images/', default = None, blank = True)
	date = models.DateTimeField(auto_now = True)
	def __str__(self):
		return str(self.id)+' '+self.name

class Buyer(models.Model):
	name = models.CharField(max_length = 50)
	uname = models.CharField(max_length = 30)
	email = models.EmailField(default = None, blank = True, null = True)
	phone = models.CharField(max_length = 20, default = None, blank = True, null = True)
	address1 = models.CharField(max_length = 100, default = None, blank = True, null = True)
	address2 = models.CharField(max_length = 100, default = None, blank = True, null = True)
	state = models.CharField(max_length = 30, default = None, blank = True, null = True)
	pin = models.CharField(max_length = 20, default = None, blank = True, null = True)
	def __str__(self):
		return str(self.id)+' '+self.name

class Cart(models.Model):
	buyer = models.ForeignKey(Buyer, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	quantity = models.IntegerField()
	total = models.IntegerField()
	color = models.CharField(max_length = 20, default = None)
	size = models.CharField(max_length = 10, default = None)
	def __str__(self):
		return str(self.id)+" "+self.buyer.name

class Checkout(models.Model):
	cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
	total = models.IntegerField()
	name = models.CharField(max_length = 50, default = None)
	phone = models.CharField(max_length = 20, default = None)
	email = models.EmailField(default = None, blank = True)
	address1 = models.CharField(max_length = 100)
	address2 = models.CharField(max_length = 100)
	city = models.CharField(max_length = 20)
	state = models.CharField(max_length = 30)
	pin = models.CharField(max_length = 20)
	notes = models.TextField()
	mode = models.CharField(max_length = 20, default = None)
	def __str__(self):
		return str(self.id)

class WishList(models.Model):
	user = models.ForeignKey(Buyer, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	def __str__(self):
		return str(self.id)

class Contact(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField()
	subject = models.CharField(max_length = 200)
	msg = models.TextField()
	def __str__(self):
		return str(self.id)+" "+self.name