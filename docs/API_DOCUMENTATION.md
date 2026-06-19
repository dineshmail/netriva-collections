# Netriva Collection API Documentation

## Base URL

/api/

---

## Categories API

### Get Categories

GET /api/categories/

Response:

{
"id": 1,
"name": "Pattu Sarees",
"slug": "pattu-sarees"
}

---

## Products API

### Get Products

GET /api/products/

### Get Single Product

GET /api/products/{id}/

### Create Product

POST /api/products/

### Update Product

PUT /api/products/{id}/

### Delete Product

DELETE /api/products/{id}/

---

## Cart API

### Get Cart

GET /api/cart/

### Add To Cart

POST /api/cart/add/

### Update Quantity

PUT /api/cart/update/

### Remove Item

DELETE /api/cart/remove/

---

## Orders API

### Create Order

POST /api/orders/

### Order History

GET /api/orders/

### Order Details

GET /api/orders/{id}/

---

## Authentication API

### Register

POST /api/auth/register/

### Login

POST /api/auth/login/

### Logout

POST /api/auth/logout/

### Profile

GET /api/auth/profile/
