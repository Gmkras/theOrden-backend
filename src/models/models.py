from typing import NamedTuple, Optional
from src.database.connection import get_connection

class Admin_users(NamedTuple):
    admin_id: Optional[int] = None
    name: Optional[str] = None
    password: Optional[str] = None
    
class Customer(NamedTuple):
    order_id: Optional[int] = None
    name: Optional[str] = None
    
class Shop(NamedTuple):
    shop_id: Optional[int] = None
    name: Optional[str] = None
    
class Category(NamedTuple):
    category_id: Optional[int] = None
    name: Optional[str] = None
    
class Product(NamedTuple):
    product_id: Optional[int] = None
    name: Optional[str] = None
    price: Optional[int] = None
    model: Optional[str] = None

class Cart(NamedTuple):
    cart_id: Optional[int] = None
    quantity: Optional[int] = None
    total_cost: Optional[int] = None
    
class Payment(NamedTuple):
    payment_id: Optional[int] = None
    amount: Optional[int] = None
    payment_type: Optional[str] = None