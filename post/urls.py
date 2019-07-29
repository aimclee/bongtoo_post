from django.urls import path
from . import views

# url : post/urlpatterns
urlpatterns = [
    path('', views.reviews, name = 'reviews'),
    path('<int:user_id>/', views.my_reviews, name = 'my_reviews'),
    path('new', views.my_reviews, name = 'my_reviews'),
    path('create', views.create, name = 'create'),
    #path(news...)
]