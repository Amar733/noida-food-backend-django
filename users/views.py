from ninja import Router
from ninja.security import HttpBearer
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from ninja_jwt.tokens import RefreshToken
from .schemas import (
    UserRegisterSchema, UserLoginSchema, UserOutSchema,
    TokenSchema, ErrorSchema, MessageSchema
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
    """Register a new user"""
    if User.objects.filter(username=payload.username).exists():
        return 400, {"error": "Username already taken"}
    
    if User.objects.filter(email=payload.email).exists():
        return 400, {"error": "Email already registered"}

    user = User.objects.create_user(
        username=payload.username,
        email=payload.email,
        password=payload.password,
        phone=payload.phone or '',
        address=payload.address or '',
    )
    
    refresh = RefreshToken.for_user(user)
    return 201, {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


@router.post("/login", response={200: TokenSchema, 401: ErrorSchema})
def login(request, payload: UserLoginSchema):
    """Login user and return JWT tokens"""
    user = authenticate(username=payload.username, password=payload.password)
    
    if not user:
        return 401, {"error": "Invalid credentials"}

    refresh = RefreshToken.for_user(user)
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
    
    for field in ['first_name', 'last_name', 'phone', 'address', 'email']:
        if field in payload:
            setattr(user, field, payload[field])
    
    user.save()
    return user

