from flask import Flask

def create_app():
    # Create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app
