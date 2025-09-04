from django.urls import path
from  . import views
urlpatterns = [
    path('', views.index, name = 'main'),
    path('about/', views.infa , name = 'about'),
    path("recipe/<str:name>/", views.recipt, name="recipt"),
]
