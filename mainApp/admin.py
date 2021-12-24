from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Buyer)
admin.site.register(Cart)
admin.site.register(Checkout)
admin.site.register(WishList)
admin.site.register(Contact)