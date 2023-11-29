from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, DateTime
from sqlalchemy.orm import validates
from sqlalchemy.sql import func 
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    zip_code = db.Column(db.integer, nullable=False)
    local_store_id = db.Column(db.Integer, db.ForeignKey('lstores.id'))
    user_cart_id = db.Column(db.Integer, db.ForeignKey('ucarts.id'))
    user_orders_id = db.Column(db.Integer, db.ForeignKey('uorders.id'))

class Store(db.Model, SerializerMixin):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    logourl = db.Column(db.String)
    

class LocalStore(db.Model, SerializerMixin):
    __tablename__ = 'local_stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    logourl = db.Column(db.String)
    zip_code = db.Column(db.integer, nullable=False)
    hours = db.Column(DateTime(timezone=True), server_default=func.now())
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

class UserCart(db.Model, SerializerMixin):
    __tablename__ = 'user_carts'

    id = db.Column(db.Integer, primary_key=True)
    cart_product = db.Column(db.Integer, db.ForeignKey('cart_products.id'))
    total = db.Column(db.Integer)
    similar_products = db.Column(db.String)
    is_logged_in = db.Column(db.Boolean, unique=False, default=True)

class CartProduct(db.Model, SerializerMixin):
    __tablename__ ='cart_products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    imgurl = db.Column(db.String)
    price = db.Column(db.Integer)
    availability = db.Column(db.Boolean, unique=False, default=True)
    quantity = db.Column(db.Integer)

class SearchProduct(db.Model, SerializerMixin):
    __tablename__ ='search_products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    imgurl = db.Column(db.String)
    price = db.Column(db.Integer)

class ResultProduct(db.Model, SerializerMixin):
    __tablename__ = "result_products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    imgurl = db.Column(db.String)
    price = db.Column(db.Integer)
    availability = db.Column(db.Boolean, unique=False, default=True)
    tags = db.Column(db.String)
    description = db.Column(db.String)
    suggested_products = db.Column(db.Integer, db.ForeignKey('suggested_products'))

class SuggestedProduct(db.Model, SerializerMixin):
    __tablename__ = 'suggested_products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    imgurl = db.Column(db.String)
    price = db.Column(db.Integer)
    availability = db.Column(db.Boolean, unique=False, default=True)
    tags = db.Column(db.String)
    description = db.Column(db.String)

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    imgurl = db.Column(db.String)
    average_consumption = db.Column(db.String)
    average_expiration = db.Column(db.String)
    tags = db.Column(db.String)
    description = db.Column(db.String)

class Fridge(db.Model, SerializerMixin):
    __tablename__ = 'fridges'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    



