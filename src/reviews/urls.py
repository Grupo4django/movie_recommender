from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_home, name='review_home'),  # Nueva URL para la ruta base
    path('<int:movie_id>/', views.review_list, name='review_list'),
    path('<int:movie_id>/create/', views.create_review, name='create_review'),
]
