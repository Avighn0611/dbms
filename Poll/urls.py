from django.urls import path, include
from Poll import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.index , name= 'home'),
    path('show_all_questions', views.show_data),
    path('add-data/', views.add_data, name='add_data'),
    path('success/', views.success_view, name='success'),  # Ensure 'success' view is defined and used correctly
]


