from flask import Flask, jsonify
from flask_cors import CORS
from routes.upload import upload_file

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)


@app.route('/')
def home():
    return jsonify({"message": "Hello World"})

app.register_blueprint(upload_file)

if __name__ == '__main__':
    app.run(debug=True)