from flask import Flask
from routes.main import main
from routes.sheets import sheets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Registrar os blueprints
app.register_blueprint(main)
app.register_blueprint(sheets)

if __name__ == '__main__':
    app.run(debug=True)
