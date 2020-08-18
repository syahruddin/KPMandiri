from flask import Flask


def create_app():
    """Create Flask application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from .auth import auth
        #from .chat import chat
        from .home import home
        from .mail import mail
        #from .project import project
        from .storage import storage
        from .query import query
        from .user import user

        # Register Blueprints
        app.register_blueprint(auth.auth_bp)
        #app.register_blueprint(chat.chat_bp)
        app.register_blueprint(home.home_bp)
        app.register_blueprint(mail.mail_bp)
        #app.register_blueprint(project.project_bp)
        app.register_blueprint(storage.storage_bp)
        app.register_blueprint(query.query_bp)
        app.register_blueprint(user.user_bp)



        return app
