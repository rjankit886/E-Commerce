from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home),
    path('cart/',cartDetails),
    path('checkout/',checkoutDetails),
    path('contact/',contactDetails),
    path('login/',loginDetails),
    path('product/<int:num>/',productDetails),
    path('shop/<str:cat>/<str:br>/',shopDetails),
    path('signup/',signupUser),
    path('profile/',profile),
    path('logout/',logout),
    path('addproduct/',addProduct),
    path('deleteproduct/<int:num>/',deleteProduct),
    path('editproduct/<int:num>/',editProduct),
    path('deletecart/<int:num>/',deleteCart),
    path('confirm/',confirm),
    path('wishlist/<int:num>/',wishlistDetails),
    path('wishlist/',wishlistBuyer),
    path('deletewishlist/<int:num>/',wishlistDelete),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
