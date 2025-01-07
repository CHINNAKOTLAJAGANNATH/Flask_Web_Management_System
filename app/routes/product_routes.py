from flask import Blueprint, request, render_template, flash, redirect, url_for
from app.models.models import Product, Category
from app.decorators import login_required
from .. import db

product = Blueprint('product', __name__)

@product.route('/products', methods=['GET'])
@login_required
def index():
    products = Product.query.all()
    return render_template('products/index.html', products=products)

@product.route('/products/create', methods=['GET', 'POST'])
@login_required
def create():
    categories = Category.query.all()
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category_id = request.form.get('category_id')
        new_product = Product(name=name, price=float(price), category_id=int(category_id))
        db.session.add(new_product)
        db.session.commit()
        flash('Product created successfully')
        return redirect(url_for('product.index'))
    return render_template('products/create.html', categories=categories)


@product.route('/product/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    prod = Product.query.get_or_404(id)
    if request.method == 'POST':
        prod.name = request.form.get('name')
        prod.price = request.form.get('price')
        prod.category_id = request.form.get('category_id')
    
        db.session.commit()
        flash('Product updated successfully')
        return redirect(url_for('product.index'))
    return render_template('products/edit.html', prod=prod)

@product.route('/product/delete/<int:id>')
@login_required
def delete(id):
    prod = Product.query.get(id)
    if not prod:
        flash('Product not found')
        return redirect(url_for('product.index'))
    db.session.delete(prod)
    db.session.commit()
    flash('Product deleted successfully')
    return redirect(url_for('product.index'))