from flask import Flask
from config import Config
from app.extensions import jwt, cors, init_database, init_elasticsearch


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)
    cors.init_app(app)

    init_database(app)
    init_elasticsearch(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.appointment_routes import appointment_bp
    from app.routes.hospital_routes import hospital_bp
    from app.routes.search_routes import search_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(appointment_bp, url_prefix="/api/appointments")
    app.register_blueprint(hospital_bp, url_prefix="/api/hospitals")
    app.register_blueprint(search_bp, url_prefix="/api/search")

    @app.route("/api/health", methods=["GET"])
    def health_check():
        return {"status": "ok", "message": "MHRS backend is running"}, 200

    return app