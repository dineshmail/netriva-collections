# Netriva Collection Database Schema

## Categories Table

Category

Fields:

* id
* name
* slug
* description
* image
* is_active
* created_at
* updated_at

---

## Products Table

Product

Fields:

* id
* category_id
* name
* description
* price
* stock
* image
* is_active
* created_at
* updated_at

Relationship:

Category (1) ---> (Many) Products

---

## Cart Table

Cart

Fields:

* id
* user_id
* created_at
* updated_at

---

## Cart Item Table

CartItem

Fields:

* id
* cart_id
* product_id
* quantity

Relationship:

Cart (1) ---> (Many) CartItems

---

## Orders Table

Order

Fields:

* id
* user_id
* total_amount
* payment_method
* status
* shipping_address
* created_at

Order Status:

* Pending
* Confirmed
* Packed
* Shipped
* Delivered
* Cancelled

---

## Order Item Table

OrderItem

Fields:

* id
* order_id
* product_id
* quantity
* price

Relationship:

Order (1) ---> (Many) OrderItems
