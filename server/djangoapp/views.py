from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import logging
import json
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create a `login_user` view to handle the sign-in request
@csrf_exempt  # Disable CSRF protection for this view
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Get the request data
        username = data.get('userName')
        password = data.get('password')

        # Authenticate user with provided credentials
        user = authenticate(username=username, password=password)

        # Prepare response data
        response_data = {"userName": username}

        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            response_data = {"userName": username, "status": "Authenticated"}
        else:
            response_data = {"status": "failure", "message": "Invalid credentials"}

        return JsonResponse(response_data)
    return JsonResponse({'status': 'failure', 'message': 'POST request required'})

# Create a `logout_request` view to handle the sign-out request
@csrf_exempt  # Disable CSRF protection for this view
def logout_request(request):
    if request.user.is_authenticated:
        # Log the user out if authenticated
        logout(request)
        return JsonResponse({'status': 'success', 'message': 'Logged out successfully'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'No user is logged in'})

# Create a `registration` view to handle sign-up request
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        email = data.get('email')

        # Validate required fields
        if not username or not password or not email:
            return JsonResponse({'status': 'failure', 'message': 'Missing required fields'})

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'failure', 'message': 'Username already exists'})

        # Create a new user
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            # Auto-login the user after successful registration
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'User created successfully', 'userName': username})
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            return JsonResponse({'status': 'failure', 'message': 'User creation failed'})

# Example view to get a list of dealerships
def get_dealerships(request):
    # Placeholder example - normally fetched from your models
    dealerships = [
        {"id": 1, "name": "Best Cars Dealership", "location": "New York"},
        {"id": 2, "name": "Luxury Cars", "location": "Los Angeles"}
    ]
    return JsonResponse({'dealerships': dealerships})

# Example view to get reviews for a dealer
def get_dealer_reviews(request, dealer_id):
    # Placeholder example - normally fetched from your models
    reviews = [
        {"review_id": 1, "dealer_id": dealer_id, "review": "Great experience!"},
        {"review_id": 2, "dealer_id": dealer_id, "review": "Highly recommend!"}
    ]
    return JsonResponse({'reviews': reviews})

# Example view to get dealer details
def get_dealer_details(request, dealer_id):
    # Placeholder example - normally fetched from your models
    dealer = {"id": dealer_id, "name": "Best Cars Dealership", "location": "New York", "contact": "123-456-7890"}
    return JsonResponse({'dealer': dealer})

# Example view to add a review
@csrf_exempt
def add_review(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dealer_id = data.get('dealer_id')
        review = data.get('review')

        # Validate required fields
        if not dealer_id or not review:
            return JsonResponse({'status': 'failure', 'message': 'Missing required fields'})

        # Here, you would save the review to your database (this is a placeholder)
        new_review = {"review_id": 1, "dealer_id": dealer_id, "review": review}

        return JsonResponse({'status': 'success', 'message': 'Review added successfully', 'review': new_review})
