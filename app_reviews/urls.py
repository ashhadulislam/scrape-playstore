from django.urls import path

from . import views


app_name="app_reviews"
urlpatterns = [
    path('', views.index, name='index'),
    path('get_reviews/', views.get_reviews, name='get_reviews'),
    path('get_reviews_csv/', views.get_reviews_csv, name='get_reviews_csv'),
]



# app_name = 'app_reviews'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
# ]