# Import Django path routing function
from django.urls import path
# Import views module from Birdie application package
from Birdie import views

# URL patterns list mapping URLs to view functions
urlpatterns = [
    # 1. Home page timeline route
    path('', views.home_view, name='home'),

    # 2. About / Goal page route (Fixes NoReverseMatch error for navbar)
    path('about/', views.about_view, name='about_our_goal'),

    # 3. User registration sign-up route
    path('register/', views.register_view, name='register'),

    # 4. User login authentication route
    path('login/', views.login_view, name='login'),

    # 5. User logout route
    path('logout/', views.logout_view, name='logout'),

    # 6. Protected profile editing route
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),

    # 7. Dynamic user profile page route by username
    path('profile/<str:username>/', views.profile_view, name='profile'),
]