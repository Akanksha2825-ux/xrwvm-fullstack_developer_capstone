from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views  # Import views from the current application

app_name = 'djangoapp'

urlpatterns = [
    # Path for registration
    path('register/', views.registration, name='register'),  # Registration API

    # Path for login
    path('login/', views.login_user, name='login'),  # Login API

    # Path for logout
    path('logout/', views.logout_request, name='logout'),  # Logout API

    # Path for getting dealer reviews (add dealer_id as a parameter)
    path('dealer_reviews/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),  # Get reviews for a specific dealer

    # Path for adding a review
    path('add_review/', views.add_review, name='add_review'),  # Add a review

    # Path for getting all dealerships
    path('get_dealerships/', views.get_dealerships, name='get_dealerships'),  # Get all dealerships

    # Path for getting details of a specific dealership
    path('dealer_details/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),  # Get details of a specific dealer

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
