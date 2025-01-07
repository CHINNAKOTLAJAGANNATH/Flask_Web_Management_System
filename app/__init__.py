from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    from .routes.index_routes import index as index_blueprint
    app.register_blueprint(index_blueprint)

    from .routes.auth_routes import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .routes.user_routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .routes.category_routes import category as category_blueprint
    app.register_blueprint(category_blueprint)

    from .routes.product_routes import product as product_blueprint
    app.register_blueprint(product_blueprint)

    with app.app_context():
        db.create_all()
        return app