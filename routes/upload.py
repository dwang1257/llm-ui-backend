import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

upload_file = Blueprint('upload_file', __name__)

UPLOAD_FOLDER = '/Users/dylan/finetuner/llm-ui-backend/uploads'
ALLOWED_EXTENSIONS = {'jsonl', 'csv'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_file.route('/upload', methods=['GET', 'POST'])
def handle_upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({"message": "No file part"})
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return jsonify({"message": "No selected file"})
        if file and allowed_file(file.filename):
            try:
                filename = secure_filename(file.filename)
                save_path = os.path.join(UPLOAD_FOLDER, filename)
                file.save(save_path)
                return jsonify({"message": "File successfully uploaded", "filename": filename})
            except:
                return jsonify({"message": "File upload failed"}), 500
    return jsonify({"message": "Upload endpoint is ready"})