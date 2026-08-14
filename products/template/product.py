"""
CRUD Operations Script for Product APIs (Chicken, Dry Fruits, Sweets)
This script provides Python classes to perform CRUD operations on product APIs

ALTERNATIVE: Use the HTML Interface
====================================
For a better visual experience, open 'product.html' in your browser!
The HTML interface provides:
- Tabbed interface for Chicken, Dry Fruits, and Sweets
- Visual forms for all CRUD operations
- Real-time response display
- Easy testing of all API endpoints

To use the HTML interface:
1. Make sure your Django server is running: python manage.py runserver
2. Open 'product.html' file in any web browser
3. Configure the Base URL and Auth Token
4. Use the tabs to switch between product categories
"""

import requests
import json


class ChickenCRUD:
    """
    Utility class to perform CRUD operations on chicken items
    Uses the chicken API endpoints from views/chicken.py
    """
    
    def __init__(self, base_url="http://localhost:8000", auth_token=None):
        """
        Initialize the CRUD client
        
        Args:
            base_url: Base URL of the API (default: http://localhost:8000)
            auth_token: Authentication token for admin operations
        """
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json'
        }
        if auth_token:
            self.headers['Authorization'] = f'Bearer {auth_token}'
    
    def get_all_chicken_items(self):
        """
        GET /products/chicken/data
        Retrieve all chicken items
        
        Returns:
            dict: {"category": "Chicken", "items": [...]}
        """
        url = f"{self.base_url}/products/chicken/data"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
    
    def create_chicken_items_bulk(self, items):
        """
        POST /products/chicken/data
        Create multiple chicken items at once
        
        Args:
            items: List of dicts [{"name": "...", "price": ..., "image": "..."}]
        
        Returns:
            dict: Created items response
        """
        url = f"{self.base_url}/products/chicken/data"
        payload = {
            "category": "Chicken",
            "items": items
        }
        
        response = requests.post(url, headers=self.headers, json=payload)
        
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
    
    def create_chicken_item(self, name, price, image):
        """
        POST /products/chicken/items
        Create a single chicken item
        
        Args:
            name: Item name
            price: Item price
            image: Image filename
        
        Returns:
            dict: Created item
        """
        url = f"{self.base_url}/products/chicken/items"
        payload = {
            "name": name,
            "price": price,
            "image": image
        }
        
        response = requests.post(url, headers=self.headers, json=payload)
        
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
    
    def update_chicken_item(self, item_name, name=None, price=None, image=None):
        """
        PUT /products/chicken/items/{item_name}
        Update a chicken item by name
        
        Args:
            item_name: Name of the item to update
            name: New name (optional)
            price: New price (optional)
            image: New image (optional)
        
        Returns:
            dict: Updated item
        """
        url = f"{self.base_url}/products/chicken/items/{item_name}"
        payload = {}
        
        if name is not None:
            payload['name'] = name
        if price is not None:
            payload['price'] = price
        if image is not None:
            payload['image'] = image
        
        response = requests.put(url, headers=self.headers, json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
    
    def delete_chicken_item(self, item_name):
        """
        DELETE /products/chicken/items/{item_name}
        Delete a chicken item by name
        
        Args:
            item_name: Name of the item to delete
        
        Returns:
            dict: Success message
        """
        url = f"{self.base_url}/products/chicken/items/{item_name}"
        response = requests.delete(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")


# ============================================================================
# USAGE EXAMPLES
# ============================================================================

if __name__ == "__main__":
    # Initialize the CRUD client
    # Replace with your actual auth token for create/update/delete operations
    crud = ChickenCRUD(
        base_url="http://localhost:8000",
        auth_token="your-auth-token-here"
    )
    
    # Example 1: Get all chicken items
    print("=== GET ALL CHICKEN ITEMS ===")
    try:
        all_items = crud.get_all_chicken_items()
        print(json.dumps(all_items, indent=2))
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Create a single chicken item
    print("\n=== CREATE SINGLE ITEM ===")
    try:
        new_item = crud.create_chicken_item(
            name="Chicken Biryani",
            price=249,
            image="chicken-biryani.jpg"
        )
        print(json.dumps(new_item, indent=2))
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Create multiple chicken items (bulk)
    print("\n=== CREATE BULK ITEMS ===")
    try:
        items_to_create = [
            {"name": "Chicken Tikka", "price": 199, "image": "chicken-tikka.jpg"},
            {"name": "Butter Chicken", "price": 299, "image": "butter-chicken.jpg"},
            {"name": "Chicken Curry", "price": 249, "image": "chicken-curry.jpg"}
        ]
        bulk_result = crud.create_chicken_items_bulk(items_to_create)
        print(json.dumps(bulk_result, indent=2))
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 4: Update a chicken item
    print("\n=== UPDATE ITEM ===")
    try:
        updated_item = crud.update_chicken_item(
            item_name="Chicken Biryani",
            price=269  # Update only the price
        )
        print(json.dumps(updated_item, indent=2))
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 5: Delete a chicken item
    print("\n=== DELETE ITEM ===")
    try:
        delete_result = crud.delete_chicken_item("Chicken Curry")
        print(json.dumps(delete_result, indent=2))
    except Exception as e:
        print(f"Error: {e}")
