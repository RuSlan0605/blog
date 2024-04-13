from django.urls import path
from .views import blog_list, blog_detail
from .views import create, update, delete
from .views import category_filter
from .views import signup, user_login



urlpatterns = [
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<int:pk>/<slug:slug>/', blog_detail, name='blog_detail'),
    path('blogs/create/', create, name='create'),
    path('blogs/<int:pk>/update/', update, name='update'),
    path('blogs/<int:pk>/delete/', delete, name='delete'),
    path('blogs/category/<int:pk>/', category_filter, name='category'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
]