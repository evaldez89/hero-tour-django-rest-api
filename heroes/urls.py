from django.urls import path
from heroes import views

urlpatterns = [
    path('heroes/', views.hero_list),
    path('heroes/<str:name>', views.hero_search),
    path('hero/<int:pk>/', views.hero_detail),
]