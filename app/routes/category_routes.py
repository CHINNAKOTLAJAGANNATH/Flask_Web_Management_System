from flask import Blueprint, request, render_template, flash, redirect, url_for
from app.models.models import Category
from app.decorators import login_required
from .. import db

category = Blueprint('category', __name__)

@category.route('/categories', methods=['GET'])
@login_required
def index():
    categories = Category.query.all()
    return render_template('categories/index.html', categories=categories)

@category.route('/categories/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        flash('Category created successfully')
        return redirect(url_for('category.index'))
    return render_template('categories/create.html')


@category.route('/category/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    cat = Category.query.get_or_404(id)
    if request.method == 'POST':
        cat.name = request.form.get('name')
        
        db.session.commit()
        flash('Category updated successfully')
        return redirect(url_for('category.index'))
    return render_template('categories/edit.html', cat=cat)

@category.route('/category/delete/<int:id>')
@login_required
def delete(id):
    cat = Category.query.get(id)
    if not cat:
        flash('Category not found')
        return redirect(url_for('category.index'))
    db.session.delete(cat)
    db.session.commit()
    flash('Category deleted successfully')
    return redirect(url_for('category.index'))