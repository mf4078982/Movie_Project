from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('movie/<int:id>/', views.movie, name='movie'),  # For viewing a specific movie by ID
    path('movie/', views.movie_list, name='movie_list'),  # For viewing a list of all movies
    path('show/', views.show, name='show'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete_movie/<int:id>/', views.delete_movie, name='delete_movie'),
    path('register/', views.register, name='register'),
    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', views.movieapp_view, name='movieapp'),
    
]
