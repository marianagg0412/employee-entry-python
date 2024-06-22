from flask import Flask
from flask_cors import CORS
from routes.employee import employee_bp
from routes.guest import guest_bp

app = Flask(__name__)
CORS(app)

# Registrar Blueprints
app.register_blueprint(employee_bp, url_prefix='/employee')
app.register_blueprint(guest_bp, url_prefix='/guest')

if __name__ == '__main__':
    app.run(debug=True)
