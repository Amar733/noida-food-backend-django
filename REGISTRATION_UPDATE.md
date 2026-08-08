# Registration Update - Phone-Based Authentication

## Changes Made

The registration and login system has been updated to use **phone-based authentication** instead of username/email-based authentication.

### Frontend Changes

#### Registration Form (`/register`)
Now requires only **3 fields**:
- **Full Name** (required)
- **Mobile Number** (required)
- **Password** (required, minimum 6 characters)

#### Login Form (`/login`)
Now requires only **2 fields**:
- **Mobile Number** (required)
- **Password** (required)

### Backend Changes

#### Registration API (`POST /api/users/register`)

**New Request Body:**
```json
{
  "full_name": "John Doe",
  "phone": "+1234567890",
  "password": "securepass123"
}
```

**Backend Processing:**
- Validates phone number is unique
- Generates username from phone number (digits only)
- Generates email as `{phone_digits}@phone.local`
- Splits full name into first_name and last_name
- Creates user with all required fields

**Response:** `201 Created`
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Error Response:** `400 Bad Request`
```json
{
  "error": "Phone number already registered"
}
```

---

#### Login API (`POST /api/users/login`)

**New Request Body:**
```json
{
  "phone": "+1234567890",
  "password": "securepass123"
}
```

**Backend Processing:**
- Looks up user by phone number
- Authenticates using username and password internally
- Returns JWT tokens

**Response:** `200 OK`
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Error Response:** `401 Unauthorized`
```json
{
  "error": "Invalid credentials"
}
```

---

### Database Changes

#### User Model
- Added **unique constraint** to `phone` field
- Migration created: `0002_alter_user_phone.py`

---

## Testing

### Test Registration

1. Start the backend server:
```bash
cd backend_Ecommerce
python manage.py runserver
```

2. Start the frontend:
```bash
cd frontend
npm run dev
```

3. Navigate to: http://localhost:3000/register

4. Fill in:
   - Full Name: `Test User`
   - Mobile Number: `+1234567890`
   - Password: `test123`

5. Submit the form

### Test Login

1. Navigate to: http://localhost:3000/login

2. Fill in:
   - Mobile Number: `+1234567890`
   - Password: `test123`

3. Submit the form

---

## API Examples

### Using cURL

**Register:**
```bash
curl -X POST http://localhost:8000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "John Doe",
    "phone": "+1234567890",
    "password": "securepass123"
  }'
```

**Login:**
```bash
curl -X POST http://localhost:8000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "phone": "+1234567890",
    "password": "securepass123"
  }'
```

---

## Migration Commands

If you need to apply migrations on a fresh database:

```bash
cd backend_Ecommerce
python manage.py migrate
```

---

## Benefits

1. **Simplified Registration**: Only 3 fields instead of 5
2. **Phone Verification Ready**: Easy to add OTP verification later
3. **No Email Requirement**: Users don't need an email address
4. **Better UX**: Faster registration process
5. **Mobile-First**: Perfect for mobile-centric users

---

## Notes

- Phone numbers must be unique in the system
- Username is auto-generated from phone digits
- Email is auto-generated as `{digits}@phone.local`
- First and last names are extracted from full name
- All existing user data remains intact
