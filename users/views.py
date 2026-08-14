from ninja import Router, Schema
from ninja.security import HttpBearer
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from ninja_jwt.tokens import RefreshToken
from .schemas import (
    UserRegisterSchema, UserLoginSchema, UserOutSchema,
    TokenSchema, ErrorSchema, MessageSchema, AdminLoginSchema
)

User = get_user_model()
router = Router()


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        from ninja_jwt.authentication import JWTAuth
        jwt_auth = JWTAuth()
        return jwt_auth.authenticate(request, token)


@router.post("/register", response={201: TokenSchema, 400: ErrorSchema})
def register(request, payload: UserRegisterSchema):
    """Register a new user with full name, phone, and password"""
    # Check if phone already exists
    if User.objects.filter(phone=payload.phone).exists():
        return 400, {"error": "Phone number already registered"}
    
    # Use phone as username (since Django requires a unique username)
    username = payload.phone
    
    # If username exists, append a number (safety check)
    base_username = username
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f"{base_username}_{counter}"
        counter += 1
    
    # Use empty email or make it optional
    email = ""
    
    # Split full name into first and last name
    name_parts = payload.full_name.strip().split(maxsplit=1)
    first_name = name_parts[0] if name_parts else ''
    last_name = name_parts[1] if len(name_parts) > 1 else ''

    user = User.objects.create_user(
        username=username,
        email=email,
        password=payload.password,
        phone=payload.phone,
        first_name=first_name,
        last_name=last_name,
        address='',
    )
    
    refresh = RefreshToken.for_user(user)
    return 201, {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


@router.post("/login", response={200: TokenSchema, 401: ErrorSchema})
def login(request, payload: UserLoginSchema):
    """Login user with phone and password and return JWT tokens"""
    try:
        # Find user by phone number
        user = User.objects.get(phone=payload.phone)
        # Authenticate using the username and password
        authenticated_user = authenticate(username=user.username, password=payload.password)
        
        if not authenticated_user:
            return 401, {"error": "Invalid credentials"}

        refresh = RefreshToken.for_user(authenticated_user)
        return 200, {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
    except User.DoesNotExist:
        return 401, {"error": "Invalid credentials"}


@router.post("/admin-login", response={200: TokenSchema, 401: ErrorSchema})
def admin_login(request, payload: AdminLoginSchema):
    """Login for admin/superuser using username and password"""
    authenticated_user = authenticate(username=payload.username, password=payload.password)
    
    if not authenticated_user:
        return 401, {"error": "Invalid credentials"}
    
    if not authenticated_user.is_staff and not authenticated_user.is_superuser:
        return 401, {"error": "Admin access required"}

    refresh = RefreshToken.for_user(authenticated_user)
    return 200, {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


@router.get("/me", response=UserOutSchema, auth=AuthBearer())
def get_current_user(request):
    """Get current authenticated user details"""
    return request.auth


@router.put("/me", response=UserOutSchema, auth=AuthBearer())
def update_profile(request, payload: dict):
    """Update user profile"""
    user = request.auth
    
    # Only allow updating these fields
    for field in ['first_name', 'last_name', 'phone', 'address']:
        if field in payload:
            setattr(user, field, payload[field])
    
    user.save()
    return user

