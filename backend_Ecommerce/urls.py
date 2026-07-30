from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ninja import NinjaAPI
from users.views import router as users_router
from products.views import router as products_router
from orders.views import router as orders_router
from payments.views import router as payments_router

# Initialize Ninja API
api = NinjaAPI(
    title="E-Commerce API",
    version="1.0.0",
    description="Complete E-Commerce Backend API with Django Ninja"
)

# Register routers
api.add_router("/users", users_router, tags=["Users"])
api.add_router("/products", products_router, tags=["Products"])
api.add_router("/orders", orders_router, tags=["Orders"])
api.add_router("/payments", payments_router, tags=["Payments"])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

