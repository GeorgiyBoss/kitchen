from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('<int:pk>', views.ProductDetail.as_view(), name='detail'),
    path('<int:pk>/delete', views.ProductDelete.as_view(), name='delete'),
    path('<int:pk>/update', views.ProductEdit.as_view(), name='edit'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart_view', views.cart_view, name='cart_view'),
    # path('decrease_cart', views.decrease_cart, name='minus'),
    path('cart/decrease/<int:product_id>', views.decrease_cart, name='decrease_cart'),
    path('cart/plus/<int:product_id>', views.plus_cart, name='plus_cart'),
    path('cart/remove/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
]