from django.urls import path
from heroes import views

urlpatterns = [
    path('heroes/', views.hero_list),
    path('hero/<int:pk>/', views.hero_detail),
]