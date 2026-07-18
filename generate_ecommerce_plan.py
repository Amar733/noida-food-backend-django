from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER

doc = SimpleDocTemplate(
    "Ecommerce_Backend_Project_Plan.pdf",
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=20, textColor=colors.HexColor('#1a1a2e'), spaceAfter=6, alignment=TA_CENTER)
subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=11, textColor=colors.HexColor('#555555'), spaceAfter=16, alignment=TA_CENTER)
h1_style = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=14, textColor=colors.HexColor('#16213e'), spaceBefore=14, spaceAfter=4)
h2_style = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=11, textColor=colors.HexColor('#0f3460'), spaceBefore=10, spaceAfter=3)
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=9.5, leftIndent=16, spaceAfter=3, bulletIndent=4)
sub_bullet_style = ParagraphStyle('SubBullet', parent=styles['Normal'], fontSize=9, leftIndent=32, spaceAfter=2, textColor=colors.HexColor('#333333'), bulletIndent=20)
note_style = ParagraphStyle('Note', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor('#888888'), leftIndent=16, spaceAfter=4, fontName='Helvetica-Oblique')

def h1(text): return Paragraph(text, h1_style)
def h2(text): return Paragraph(text, h2_style)
def b(text): return Paragraph(f"• {text}", bullet_style)
def sb(text): return Paragraph(f"◦ {text}", sub_bullet_style)
def note(text): return Paragraph(f"Note: {text}", note_style)
def space(n=6): return Spacer(1, n)
def hr(): return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc'), spaceAfter=6, spaceBefore=4)

content = []

# Title
content += [
    Paragraph("Django E-Commerce Backend", title_style),
    Paragraph("Complete Project Plan &amp; Step-by-Step Guide", subtitle_style),
    hr(),
    space(4),
]

# ── PHASE 1 ──────────────────────────────────────────────
content += [
    h1("Phase 1 — Project Setup"),
    h2("1.1 Environment &amp; Django Project"),
    b("Create a virtual environment and activate it"),
    sb("python -m venv venv  →  venv\\Scripts\\activate (Windows)"),
    b("Install core dependencies"),
    sb("pip install django djangorestframework djangorestframework-simplejwt django-filter pillow python-decouple"),
    b("Start Django project: django-admin startproject ecommerce_backend"),
    b("Create apps: python manage.py startapp users products orders payments"),
    b("Add all apps + 'rest_framework' + 'django_filters' to INSTALLED_APPS"),
    space(),

    h2("1.2 Settings Configuration"),
    b("Use python-decouple: move SECRET_KEY, DEBUG, DB credentials to .env file"),
    b("Configure DATABASES for PostgreSQL (recommended for production)"),
    sb("pip install psycopg2-binary"),
    b("Set MEDIA_ROOT and MEDIA_URL for product image uploads"),
    b("Configure REST_FRAMEWORK default authentication and permission classes"),
    b("Set SIMPLE_JWT settings: access token lifetime, refresh token lifetime"),
    space(),

    h2("1.3 Project Folder Structure"),
    b("ecommerce_backend/  — project config (settings, urls, wsgi)"),
    b("users/              — custom user model, auth, profiles"),
    b("products/           — categories, products, reviews"),
    b("orders/             — cart, order, order items"),
    b("payments/           — payment records, status tracking"),
    hr(),
]

# ── PHASE 2 ──────────────────────────────────────────────
content += [
    h1("Phase 2 — Custom User Model &amp; Authentication"),
    h2("2.1 Custom User Model (users app)"),
    b("Create AbstractUser subclass with extra fields:"),
    sb("phone_number, address, profile_picture, is_seller (BooleanField)"),
    b("Set AUTH_USER_MODEL = 'users.User' in settings BEFORE first migration"),
    b("Run: python manage.py makemigrations &amp;&amp; python manage.py migrate"),
    space(),

    h2("2.2 Auth Endpoints (JWT)"),
    b("POST /api/auth/register/   — create new user account"),
    b("POST /api/auth/login/      — returns access + refresh JWT tokens"),
    b("POST /api/auth/token/refresh/ — refresh access token"),
    b("GET/PUT /api/auth/profile/ — view and update own profile"),
    b("POST /api/auth/logout/     — blacklist refresh token"),
    note("Use djangorestframework-simplejwt TokenObtainPairView for login"),
    space(),

    h2("2.3 Permissions"),
    b("IsAuthenticated — for cart, orders, profile"),
    b("IsAdminUser    — for product/category create, delete"),
    b("Custom IsSeller permission — sellers can manage their own products"),
    hr(),
]

# ── PHASE 3 ──────────────────────────────────────────────
content += [
    h1("Phase 3 — Products &amp; Categories"),
    h2("3.1 Models"),
    b("Category model: name, slug, description, parent (self ForeignKey for sub-categories)"),
    b("Product model fields:"),
    sb("name, slug, description, price, discount_price, stock, is_active"),
    sb("category (ForeignKey), seller (ForeignKey to User), image (ImageField)"),
    sb("created_at, updated_at (auto timestamps)"),
    b("ProductImage model — multiple images per product (ForeignKey to Product)"),
    b("Review model: product, user, rating (1-5), comment, created_at"),
    space(),

    h2("3.2 API Endpoints"),
    b("GET    /api/products/           — list all active products"),
    b("POST   /api/products/           — create product (seller/admin only)"),
    b("GET    /api/products/{slug}/    — product detail"),
    b("PUT    /api/products/{slug}/    — update product (owner/admin only)"),
    b("DELETE /api/products/{slug}/    — delete product (owner/admin only)"),
    b("GET    /api/categories/         — list all categories"),
    b("GET    /api/products/{id}/reviews/ — list reviews for a product"),
    b("POST   /api/products/{id}/reviews/ — add review (authenticated users)"),
    space(),

    h2("3.3 Filtering, Search &amp; Pagination"),
    b("Use django-filter: filter by category, price range, in-stock"),
    b("Use SearchFilter: search by name, description"),
    b("Use OrderingFilter: sort by price, created_at, rating"),
    b("Set PAGE_SIZE = 12 in REST_FRAMEWORK settings"),
    hr(),
]

# ── PHASE 4 ──────────────────────────────────────────────
content += [
    h1("Phase 4 — Cart &amp; Orders"),
    h2("4.1 Cart Models"),
    b("Cart model: user (OneToOneField), created_at"),
    b("CartItem model: cart (ForeignKey), product (ForeignKey), quantity"),
    space(),

    h2("4.2 Cart Endpoints"),
    b("GET    /api/cart/              — view current user's cart"),
    b("POST   /api/cart/items/        — add item to cart"),
    b("PUT    /api/cart/items/{id}/   — update item quantity"),
    b("DELETE /api/cart/items/{id}/   — remove item from cart"),
    b("DELETE /api/cart/clear/        — clear entire cart"),
    space(),

    h2("4.3 Order Models"),
    b("Order model fields:"),
    sb("user, status (pending/confirmed/shipped/delivered/cancelled)"),
    sb("total_price, shipping_address, created_at, updated_at"),
    b("OrderItem model: order, product, quantity, price (snapshot at order time)"),
    space(),

    h2("4.4 Order Endpoints"),
    b("POST /api/orders/           — place order from cart (clears cart after)"),
    b("GET  /api/orders/           — list user's own orders"),
    b("GET  /api/orders/{id}/      — order detail"),
    b("PUT  /api/orders/{id}/status/ — update status (admin only)"),
    b("POST /api/orders/{id}/cancel/ — cancel order (user, if still pending)"),
    hr(),
]

# ── PHASE 5 ──────────────────────────────────────────────
content += [
    h1("Phase 5 — Payments"),
    h2("5.1 Payment Model"),
    b("Payment model fields:"),
    sb("order (OneToOneField), amount, method (card/cod/upi)"),
    sb("status (pending/success/failed), transaction_id, paid_at"),
    space(),

    h2("5.2 Payment Endpoints"),
    b("POST /api/payments/initiate/  — initiate payment for an order"),
    b("POST /api/payments/verify/    — verify payment (webhook or manual)"),
    b("GET  /api/payments/{order_id}/ — get payment status"),
    space(),

    h2("5.3 Payment Gateway (Optional Integration)"),
    b("Razorpay (India) or Stripe (International)"),
    sb("pip install razorpay  OR  pip install stripe"),
    b("Store only transaction_id, never store raw card data"),
    b("Use webhook endpoint to receive payment confirmation from gateway"),
    hr(),
]

# ── PHASE 6 ──────────────────────────────────────────────
content += [
    h1("Phase 6 — Admin &amp; Additional Features"),
    h2("6.1 Django Admin"),
    b("Register all models: User, Product, Category, Order, Payment"),
    b("Customize admin list_display, list_filter, search_fields for each model"),
    b("Add admin actions: mark orders as shipped, bulk delete inactive products"),
    space(),

    h2("6.2 Additional Features (Bonus)"),
    b("Wishlist — user can save products for later"),
    b("Coupon/Discount codes — apply discount at checkout"),
    b("Email notifications — order confirmation via Django send_mail"),
    b("Stock management — auto-reduce stock on order, block if out of stock"),
    b("Seller dashboard — seller sees only their own products and orders"),
    hr(),
]

# ── PHASE 7 ──────────────────────────────────────────────
content += [
    h1("Phase 7 — Testing"),
    h2("7.1 Unit &amp; API Tests"),
    b("Use Django TestCase + DRF APIClient"),
    b("Test user registration, login, token refresh"),
    b("Test product CRUD with different user roles"),
    b("Test cart add/remove/clear flow"),
    b("Test full order placement flow end-to-end"),
    b("Run tests: python manage.py test"),
    space(),

    h2("7.2 Manual Testing with Postman"),
    b("Create a Postman collection with all endpoints"),
    b("Set up environment variables for base URL and JWT token"),
    b("Test all happy paths and error cases (401, 403, 404, 400)"),
    hr(),
]

# ── PHASE 8 ──────────────────────────────────────────────
content += [
    h1("Phase 8 — Deployment"),
    h2("8.1 Pre-Deployment Checklist"),
    b("Set DEBUG = False in production"),
    b("Set ALLOWED_HOSTS to your domain"),
    b("Use environment variables for all secrets (.env)"),
    b("Run: python manage.py collectstatic"),
    b("Switch to PostgreSQL database"),
    space(),

    h2("8.2 Deploy on Render (Free &amp; Easy)"),
    b("Push project to GitHub"),
    b("Create a new Web Service on render.com, connect GitHub repo"),
    b("Set environment variables in Render dashboard"),
    b("Add build command: pip install -r requirements.txt &amp;&amp; python manage.py migrate"),
    b("Add start command: gunicorn ecommerce_backend.wsgi"),
    b("Add PostgreSQL database from Render dashboard, link via DATABASE_URL"),
    space(),

    h2("8.3 requirements.txt"),
    b("django, djangorestframework, djangorestframework-simplejwt"),
    b("django-filter, pillow, python-decouple, psycopg2-binary, gunicorn"),
    hr(),
]

# ── SUMMARY TABLE ─────────────────────────────────────────
content += [
    h1("Quick Reference — All API Endpoints"),
    h2("Auth"),
    b("POST /api/auth/register/  |  POST /api/auth/login/  |  POST /api/auth/token/refresh/"),
    b("GET/PUT /api/auth/profile/  |  POST /api/auth/logout/"),
    h2("Products"),
    b("GET/POST /api/products/  |  GET/PUT/DELETE /api/products/{slug}/"),
    b("GET /api/categories/  |  GET/POST /api/products/{id}/reviews/"),
    h2("Cart"),
    b("GET /api/cart/  |  POST /api/cart/items/  |  PUT/DELETE /api/cart/items/{id}/"),
    h2("Orders"),
    b("POST/GET /api/orders/  |  GET /api/orders/{id}/  |  PUT /api/orders/{id}/status/"),
    h2("Payments"),
    b("POST /api/payments/initiate/  |  POST /api/payments/verify/  |  GET /api/payments/{order_id}/"),
    space(12),
    hr(),
    Paragraph("Generated for Django E-Commerce Backend Project Plan", note_style),
]

doc.build(content)
print("PDF generated: Ecommerce_Backend_Project_Plan.pdf")
