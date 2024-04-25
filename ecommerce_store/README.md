
# Ecommerce store Flask Application

This repository contains a simple Flask application that implements an API for managing shopping carts and purchases. It also includes unit tests to ensure the functionality of the application.

## Folder Structure

```
ecommerce_store/
│
├── app.py            
├── test_app.py        
└── README.md          
```

## How to Run

### Prerequisites

Make sure you have Python and Flask installed on your system.

```bash
pip install Flask
```

### Running the Flask Application

1. **Navigate to the project directory:**

   ```bash
   cd ecommerce_store/
   ```

2. **Run the Flask application:**

   ```bash
   python app.py
   ```

   This command will start the Flask application locally.

### Accessing the API Endpoints

Once the Flask application is running, you can access the following API endpoints using tools like cURL, Postman, or a web browser:

- **Add Item to Cart**:
  ```
  POST http://127.0.0.1:5000/api/add-to-cart
  JSON Body: {"user_id": 1, "item": "product1"}
  ```

- **View Cart**:
  ```
  GET http://127.0.0.1:5000/api/view-cart?user_id=1
  ```

- **Checkout**:
  ```
  POST http://127.0.0.1:5000/api/checkout
  JSON Body: {"user_id": 1}
  ```

- **View Purchase Statistics** (Requires Admin Authorization):
  ```
  GET http://127.0.0.1:5000/api/purchase-statistics
  Headers: {"Authorization": "Bearer your_admin_token_here"}
  ```

### Running Unit Tests

1. **Navigate to the project directory:**

   ```bash
   cd project/
   ```

2. **Run the unit tests:**

   ```bash
   python test_app.py
   ```

   This command will execute the unit tests defined in `test_app.py` to ensure the functionality of the Flask application.

