from django.urls import path
from API import views

urlpatterns = [
    path('Quiz_API/', views.Quiz_API_list),
    # path('Quiz_API/<int:pk>/', views.Quiz_API_detail),
]