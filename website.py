pip install Flask
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return 'Welcome to the E-commerce Website'

@app.route('/products')
def products():
    # Display a list of products here
    return 'List of Products'

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Display the details of a product based on the product_id
    return f'Details of Product {product_id}'

@app.route('/cart')
def cart():
    # Display the contents of the shopping cart
    return 'Shopping Cart'

@app.route('/checkout')
def checkout():
    # Implement the checkout process here
    return 'Checkout Page'
