from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    # 🔑 Needed for session management
    app.secret_key = os.getenv("SECRET_KEY", "fallback-dev-key")  

    # Import & register blueprints
    from app.routes.chat import chat_bp
    from app.routes.summarize import summarize_bp
    from app.routes.preferences import preferences_bp
    from app.routes.history import history_bp

    app.register_blueprint(chat_bp)
    app.register_blueprint(summarize_bp, url_prefix="/summarize")
    app.register_blueprint(preferences_bp, url_prefix="/preferences")
    app.register_blueprint(history_bp, url_prefix="/history")

    # 📌 Add index route
    @app.route("/")
    def index():
        return render_template("index.html")

    return app
