from flask import Blueprint, render_template, url_for, session, redirect, flash
from flask import current_app as app
from webapp.func import checkArgs
from werkzeug.utils import secure_filename    #buat keamanan path pas upload


ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}


storage_bp = Blueprint('storage_bp', __name__, template_folder='templates',static_folder='static')

#coba upload file
@storage_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('storage_bp.uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
@storage_bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


#buat cek dan batasin file yg boleh di upload cuman yg disetujuin
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
