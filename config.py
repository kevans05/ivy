import os
basedir = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SECURITY_PASSWORD_SALT = 'my_precious_two'

UPLOADED_PATH=os.path.join(basedir, 'uploads')
# Flask-Dropzone config:
DROPZONE_ALLOWED_FILE_TYPE='.pdf'
DROPZONE_MAX_FILE_SIZE=3
DROPZONE_MAX_FILES=3





