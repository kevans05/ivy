import os
from flask_wtf.csrf import CSRFProtect

basedir = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SECURITY_PASSWORD_SALT = 'my_precious_two'

UPLOADED_PATH=os.path.join(basedir, 'uploads')
# Flask-Dropzone config:
DROPZONE_ALLOWED_FILE_CUSTOM=True
DROPZONE_ALLOWED_FILE_TYPE='image/*, .pdf, .txt'
DROPZONE_MAX_FILE_SIZE=3
DROPZONE_MAX_FILES=3
DROPZONE_IN_FORM=True
DROPZONE_UPLOAD_ON_CLICK=True
#DROPZONE_UPLOAD_ACTION='handle_upload_add_a_meter'  # URL or endpoint
DROPZONE_UPLOAD_BTN_ID='submit'
DROPZONE_ENABLE_CSRF=True
DROPZONE_DEFAULT_MESSAGE='Drop or Click to Upload Meter Documentation'





