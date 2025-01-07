from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.models import User
from app.decorators import login_required
from .. import db

main = Blueprint('main', __name__)

@main.route('/user')
@login_required
def index():
    users = User.query.all()
    return render_template('user/index.html', users=users)

@main.route('/user/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        new_user = User(name=name, email=email, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('User created successfully')
        return redirect(url_for('main.index'))
    return render_template('user/create.html')

@main.route('/user/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form.get('name')
        user.email = request.form.get('email')
        db.session.commit()
        flash('User updated successfully')
        return redirect(url_for('main.index'))
    return render_template('user/edit.html', user=user)

@main.route('/user/delete/<int:id>')
@login_required
def delete(id):
    user = User.query.get(id)
    if not user:
        flash('User not found')
        return redirect(url_for('main.index'))
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully')
    return redirect(url_for('main.index'))